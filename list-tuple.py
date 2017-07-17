#list	是用[]，tuple	是用();
#		可以更改，		不可以更改，初始化时确认元素

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
]
a=('abc',25,L)
#tuple a的元素并没有改变，a[2]依然指向L，改变的是list L的内容
a[2][1][3]='qiao'

print(a[1])
#打印Apple
print(L[0][0])
#打印L的最后一个元素的最后一个
print(a[2][1][3])
