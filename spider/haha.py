# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 16:21:45 2014

@author: shunxu
"""

def sort_words(words):
    """Sortd the words"""
    return sorted(words)
    
words = ['What', 'is', 'your', 'name?']

def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0)
    return word

print print_first_word(words)
print words

from sys import argv
script, filename = argv

txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(filename)
print txt_again.read()


from sys import argv
script, user_name = argv
prompt = '>'

print "Hi %s, I'm THE %s script." % (user_name, script)
print "I'd like to ask you a few questiongs."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer.Nice.
""" % (likes,lives,computer)

from sys import argv

script, first, second, third = argv

print




















































