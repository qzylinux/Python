#!/usr/bin/env python3
#encoding-utf-8

#****************动态创建类****************************
#type返回的是对象的类型，也可以用来“动态”创建对象

def  hello(self,works):
	print('hello,%s'%works)
	
#type()传入三个参数：类名，继承的父类（tuple类型，如果tuple只有一个元素时，记得最后的‘,’），方法
myclass=type('qzy',(object,),dict(fun=hello))
print(myclass)
#myclass 是一个类，所以现在实例化
my=myclass()
my.fun('zhiyuan')


#******************元类*******************************
#metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。
#正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。