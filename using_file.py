file = open("novel.txt")

count = {}

for line in file:
	line = line.strip()
	words = line.split()
	for word in words:
		if word in count:
			count[word] += 1
		else:
			count[word] = 1

#print count

list = []

for word in count:
	list.append((count[word],word))

list.sort(reverse = True)

for k,v in list[:10]:
    print v,k