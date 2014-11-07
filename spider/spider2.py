# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 14:53:12 2014

@author: shunxu
"""

import re
import urllib
import urlparse
from sgmllib import SGMLParser

class UrlDigger(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self, attrs):
        for k, v in attrs:
            if k == "href":
                self.urls.append(v.strip())

    def start_script(self, attrs):
        for k, v in attrs:
            if k == "src":
                self.urls.append(v.strip())

class Spider():
    def __init__(self):
        self.__blacklist = []
        self.__whitelist = []

    def add_blacklist(self, black_pattern):
        pattern = re.compile(black_pattern, re.IGNORECASE)
        self.__blacklist.append(pattern)

    def add_whitelist(self, white_pattern):
        pattern = re.compile(white_pattern, re.IGNORECASE)
        self.__whitelist.append(pattern)

    def __InBlacklist(self, url):
        for v in self.__blacklist:
            if v.search(url):
                return True
        return False

    def __InWhitelist(self, url):
        for v in self.__whitelist:
            if v.search(url):
                return True
        return False

    def __InitCheckBlackAndWhiteListValid(self):
        # blacklist and whitelist can not both exist!
        if len(self.__blacklist) and len(self.__whitelist):
            return False
        return True

    def __CheckUrlInFilter(self, url):
        if (not self.__InWhitelist(url)) or self.__InBlacklist(url):
            return False
        return True

    def __BFS(self, callback, start_url, max_times):
        urldigger = UrlDigger()
        urls = [start_url]
        cnt = 0
        index_in = 0
        index_out = 0

        while index_out <= index_in:
            if cnt >= max_times or len(urls) == 0:
                break

            urldigger.reset()
            cnt += 1
            base_url = urls[index_out]
            index_out += 1

            # check if in whitelist
            if len(self.__whitelist) and not self.__InWhitelist(base_url):
                callback(cnt, False, base_url, " ... Skip (url not in whitelist)")
                continue

            # check if in blacklist
            if self.__InBlacklist(base_url):
                callback(cnt, False, base_url, " ... Skip (url in blacklist)")
                continue

            try:
                usock = urllib.urlopen(base_url)
            except:
                callback(cnt, False, base_url)
                continue

            callback(cnt, True, base_url)

            try:
                url_file_content = usock.read()
                urldigger.feed(url_file_content)
            except:
                callback(cnt, False, base_url, " ... Skip (read or parse exception)")
                continue

            usock.close()

            for url_from_digger in urldigger.urls:
                full_url = urlparse.urljoin(base_url, url_from_digger)
                if urls.count(full_url) == 0:
                    urls.append(full_url)
                    index_in += 1

        urldigger.close()
        return True

    def run(self, callback, start_url, max_times = 1000):
        if not self.__InitCheckBlackAndWhiteListValid():
            print "Cannot set blacklist and whitelist at the same time!"
            return False

        return self.__BFS(callback, start_url, max_times)

def spider_callback(index, open_result, url, comment = None):
    if comment:
        print index, open_result, url, comment
    else:
        print index, open_result, url

if __name__ == "__main__":
    spider = Spider()
    spider.run(spider_callback, "http://www.qq.com")