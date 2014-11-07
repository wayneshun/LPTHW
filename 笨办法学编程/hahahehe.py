def f(n):
    f(n)=f(n-1)+f(n-2)
    f(1)=1
	f(2)=2
	return f(n)

print f(3)