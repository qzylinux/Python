#计算点的移动
#-------encoding:utf-8------------
import math
def MovePoint(x,y,step,angle=0):
	if not isinstance(x,(int,float))|isinstance(y,(int,float))|isinstance(step,(int,float))|isinstance(angle,(int,float)):
		print('the type x or y is not int or float!')
	angle=angle*math.pi/180
	nx=x+step*math.cos(angle)
	ny=y+step*math.sin(angle)
	return nx,ny

	
x=input('please input your original pointer(x):')
x=float(x)
y=input('please input your original pointer(y):')
y=float(y)
step=input('please input your step:')
step=float(step)
angle=input('please input your angle:')
angle=float(angle)
r=MovePoint(x,y,step,angle)
print(r)