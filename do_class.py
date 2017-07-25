#!/usr/bin/env python3
#encoding-utf-8

'do_class test'

__author__='qzy'

#****************************私有变量*****************************************
class student(object):
	#_init__函数是初始化函数，
	def __init__(self,name,score):
		#'__xx'定义私有变量属性，并赋值
		#外部不可以访问，一般'_xx'也不要外部访问，
		self.__name=name
		self.__score=score
		
	#将对内部变量__score的操作封装在类内部	
	def set_score(self,score):
		self.__score=score
	
	#返回内部变量的值
	def get_score(self):
		return self.__score
	def get_name(self):
		return self.__name

if __name__=='__main__':
	li=student('qzy',99)		
	print(li.get_name())
	print(li.get_score())

	
li=student('li',98)
print(li.get_name())
print(li.get_score())
print(li.set_score(88))


#***************************继承********************************************
#定义一个继承于student的类，什么都不做就拥有了student的所有
class pupil(student):
	pass

qiao=pupil('qiao',80)
print(qiao.get_score())

#当子类的属性和方法和父类冲突时，子类的会覆盖父类
class middle(student):
	def get_score(self):
		print('hh')

zhi=middle('zhi',10)
print(zhi.get_name())
print(zhi.get_score())

#**********************多态*********************************************
#类是数据类型，既是父类的类型也是子类的类型
print('qiao is a student:',isinstance(qiao,student))
print('qiao is a pupil:',isinstance(qiao,pupil))