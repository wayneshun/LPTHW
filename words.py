words = ['hello','world!','pythoner']

lst = []

for word in words:
    lst.append((len(word),word))

lst.sort(reverse = True)

sort_words = []

for i in lst:
    length,word = i
    sort_words.append(word)
print sort_words

words.sort(key = lambda x:len(x),reverse = True)

print words