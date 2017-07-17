a='start'
while a!='end':
	a=input('please input your weight:')
	#判断输入的是数字还是其他
	if a.isdigit():
		#将input的输入str类型转换为int(需要的类型)
		weight=int(a)
		#输出转换后的数字
		print('you input a float is %d.'%weight)
		#判断体重类型
		if weight<18.5:
			print('you are underweight.')
			#continue
		elif weight<=25:
			print('your weight is normal.')
			#continue
		elif weight<=28:
			print('you are overweight.')
			#continue
		elif weight<=32:
			print('you are fat.')
			#continue
		else:
			print('you are seriously fat.')
			#continue
	#输入的不是数字时提示用户
	else:
		print('you input is not digit:%s'%a)
		
#提醒用户测试完毕
print('test is over!')