def swap(lst,a,b):
    tmp = lst[a]
    lst[a] = lst[b]
    lst[b] = tmp
	
x = [10,20,30]

swap(x,0,1)
print x

nums = []

for i in range(10):
    num = float(raw_input())
    nums.append(num)

print sum(nums)/len(nums)