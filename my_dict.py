f1 = open("iPhone6.txt")
r_1 = f1.read()


f2 = open("iPhone6 Plus.txt",'w')
w_1 = f2.write(r_1)

f1.close()
f2.close()

