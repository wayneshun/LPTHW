# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 22:37:27 2014

@author: shunxu
"""

def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sortd the words"""
    return sorted(words)
        
def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the worted words"""
    words = break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    """Print the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
    
    

sentence = "All good things come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
    