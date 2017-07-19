#generator 返回当前值，并计算下一个值

def mygenerator(max):
	a,b,n=0,1,0
	while n<max:
		yield  b
		a,b=b,a+b
		n=n+1
	return 'done'
	
f=mygenerator(10)
print('mygenerator(10):',f)
for x in f:
	print(x)