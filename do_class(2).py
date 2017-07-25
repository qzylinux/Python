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
a.male=man
print(a.male)

#定义一个方法（函数）
def set_score(self,score):
	self.score=score
#将定义的方法绑定给类
student.set_score=set_score

#实例可以使用类绑定后的‘方法’
a.set_score(80)
print(a.score)


