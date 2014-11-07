myfile = open('myfile.txt')
x = myfile.read()
print x

myfile = open('myfile.txt')
for line in myfile:
    print line,