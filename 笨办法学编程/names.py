def is_name(string):
    if len(string) < 2:
        return True
        
    if string[0] != string[-1]:
        return False
    else:
        return is_name(string[1:-1])



f = open("name.txt")

for line in f:
    t = line.strip()
    if is_name(t):
        print t
	
f.close()


f = open('name.txt')

for line in f:
    name = line.strip()
    name = line.title()
    print name
	

	
	
f = open('names.txt')

for t in f:
#    name = t.strip()
    print t.title()
	
f.close()



def is_up(string):
    p = string[0]
    c = string[1]
    for c in string:
        if p > c:
            return False
        else:
            p = c
    return True


f = open('names.txt')

for line in f:
    name = line.strip()
    if is_up(name):
        print name