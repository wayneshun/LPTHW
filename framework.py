x = input('Input: ')
 
low = 0
high = x

ans = (low + high) / 2.0

while ans**2 != x:
    if ans**2 < x:
        low = ans + 1
    else:
        high = ans - 1
        
    ans = (low + high) / 2.0
 
print ans