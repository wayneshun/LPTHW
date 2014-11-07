import re

f = open("names.txt")

pattern = 'C.A'

for line in f:
    name = line.strip()
    result = re.search(pattern,name)
    if result:
        print name

f.close()