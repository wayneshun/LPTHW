import urllib
proxies = {'http': 'http://proxy.tencent.com:8080'}
filehandle = urllib.urlopen("http://www.qq.com", proxies=proxies)
print(filehandle.read())