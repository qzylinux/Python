#sorted
#encoding:utf-8

from operator import itemgetter

#字符串排序，统一为小写后按字母表排序
L=['qiao','ZHi','yuaN']
#高阶函数（函数内引用其他函数）
L1=sorted(L,key=str.lower,reverse=False)
print(L1)
#按ASCII码排序
L2=sorted(L)
print(L2)

#students是一个list，他的每个元素是tuple
students=[('qiao',80),('zhi',88),('yuan',70)]
#itemgetter用来提取维度数据
L3=sorted(students,key=itemgetter(0))
print(L3)
#提取第二维数据
L4=sorted(students,key=lambda x:x[1],reverse=True)
print(L4)
