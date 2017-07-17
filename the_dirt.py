#dirt and  set  test
#键值的存储是读取方便，占用内存大，键值不能为变量（可以为str和int）
a={
	'qiao':25,
	'li':26,
	'xiaoqiao':0,
	'xiaoting':1
};

print('a[\'qiao\']:%s'%a['qiao'])
print('a[\'li\']:',a['li'])
#如果xiaoqiao是dirt内的一个键，则返回对应的值，否则返回-1
print('a.get(\'xiaoqiao\'):',a.get('xiaoqiao',-1))

#插入一个键值对,直接输入就可以了
a['school']='HDU'
print('a[\'school\']:%s'%a['school'])
#删除一个键值
a.pop('xiaoting')
print('a.get(\'xiaoting\'):',a.get('xiaoting',-2))