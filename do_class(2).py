#！/usr/bin/env python3
#****encoding-utf-8***********

'do_class (Ⅱ)'

__author__='qzy'

#************************面向对象高级编程*****************************

#************************绑定属性与方法以及__slot__限定***************
class student(object):
	__slot__=('name','age')

class grade(student):
	__slot__=('score')

#__slot__在子类和父类中均有，那么子类允许绑定的是合集	
a=grade()
a.score=99
print(a.score)
#male不在__slot__允许范围内所以会报错
#a.male=man
#print(a.male)

#定义一个方法（函数）
def set_score(self,score):
	self.score=score
#将定义的方法绑定给类
student.set_score=set_score

#实例可以使用类绑定后的‘方法’
a.set_score(80)
print(a.score)

#*********************多重继承*****************************************
#**************允许多重继承的设计为MixIn*******************************

class  work(object):
	def set_solar(self,solar):
		self.solar=solar

class  human(student,work):
	pass

#worker同时继承了work和student的属性和方法
worker=human()
worker.name='qiaozhiyuan'
print(worker.name)
worker.set_solar(15000)
print(worker.solar)

#*****************************枚举类*********************************
from enum  import Enum,unique

#装饰器，判断weekdays里面有无重复的value
@unique
#继承自Enum的类
class weekdays(Enum):
	mon=1
	tue=2
	wed=3
	thu=4
	fri=5
	sat=6
	sun=7

print(weekdays.mon)
print(weekdays['tue'])
print(weekdays(1))
print(weekdays.sun.value)

#可以直接使用Enum类实例化,member是tuple
day=Enum('week',('mon','tue','wed','thu','fri','sat','sun'))
for name,member in day.__members__.items():
	print(name ,'=>',member,':',member.value)