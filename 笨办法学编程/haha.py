from sys import argv

script, filename = argv

text = open(filename, 'w')

line1 = raw_input("line1:")

text.write(line1)
raw_input("?")

text = open(filename)
print text.read()
text.close()

