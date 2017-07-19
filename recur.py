#汉诺塔迭代
def	hanoi(n,a,b,c):
	if n==1:
		print('move ',a,'->',c)
	else:
		hanoi(n-1,a,c,b)
		hanoi(1,a,b,c)
		hanoi(n-1,b,a,c)

hanoi(3,'A','B','C')

#阶乘迭代
def fact(n):
	if n==1:
		return n
	else:
		return fact(n-1)*n
	
print('fact(2):',fact(2))
print('fact(5):',fact(5))