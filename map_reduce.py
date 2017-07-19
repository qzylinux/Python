#map/reduce将str转为Int然后转为一个整数

from  functools  import  reduce

def str2num(s):
	#pass
	def f(x,y):
		return x*10+y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

	return reduce(f,map(char2num,s))
#f(x,y)可以使用lambda简化
#	return reduce(lambda x,y : x*10+y, map(char2num, s) )


print(str2num('123'))