f = open("iceall.txt")

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

for word in count:
    word_freq.append((count[word],word))

word_freq.sort(reverse = 1)


for t,word in word_freq[:10]:
    print word,t