#!/usr/bin/env python3
# encoding utf-8

'use pickle'
__author__='qzy'

import pickle
#序列化：内存内的变量通过pickle.pump转为bytes存放到file-like-object中
d=dict(a=20,b=30,c=49)
print(d)
with open('pickle.txt','wb') as f:
	pickle.dump(d,f)

#反序列化：将file-like-object中序列化的bytes转为变量内容
with open('pickle.txt','rb') as fi:
	da=pickle.load(fi)
	print(da)