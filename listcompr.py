#列表生成式的使用,[]生成的是list类型

#x的平方，x是1-10的奇数
print([x*x for x in range(1,11) if x%2!=0])

#把dir里的Items显示为相等
d={'a':'A','b':'B','c':'C'}
print([a+'='+b for a,b in d.items()])

#把列表中的大写转为小写
L=['Qiao','Zhi','Yuan']
print([s.lower() for s in L])