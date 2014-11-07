x = input('Input: ')
 
low = 0
high = x

ans = (low + high) / 2.0

count = 1
 
while ans**2 != x and count >= 100 :
    if ans**2 < x:
        low = ans
    else:
        high = ans
		
    ans = (low + high) / 2.0
    count += 1
 
print ans