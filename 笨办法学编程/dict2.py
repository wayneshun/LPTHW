f = open("heha.txt")

count = {}

for line in f:
    line = line.strip()
    words = line.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

word_freq = []

for word,freq in count.items():
    word_freq.append((freq,word))

word_freq.sort(reverse = True)

for freq,word in word_freq[50:100]:
    print word,freq