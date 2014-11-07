def has_no_e(word):
	for letter in word:
		if letter == 'e':
			return False
	return True

file = open("words.txt")

for line in file:
	word = line.strip()
	if has_no_e(word):
		print word