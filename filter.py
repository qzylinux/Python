#filter(函数，序列)，使用惰性计算，只有取filter得结果时才会返回值
#生成器生成序列，然后用生成器（generator）和过滤器（filter）返回新的序列
#其中新序列的生成原则是：序列每一个元素除以序列的第一个元素，整除的过滤掉

def odd_iter():
	n=1
	while True:
		n=n+2
		yield n		
		
def prime_filter(n):
	return lambda x : x%n>0
		
def primenumber():
	yield 2
	t=odd_iter()
	while True:
		n=next(t)
		yield n
		t=filter(prime_filter(n),t)

def main():
	for x in primenumber():
		if x<1000:
			print(x)
		else :
			break
	
if __name__ == '__main__':
	main()