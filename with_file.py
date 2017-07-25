#!/usr/bin/env python3
#encoding-utf-8

from datetime import datetime

with open('test.txt','w',encoding='utf-8') as fi:
	for n in range(10):
		fi.write('今天是：')
		fi.write(datetime.now().strftime('%Y-%m-%d'))
		fi.write('\n')


with open('test.txt','r',errors='ignore') as fi:
	a=fi.read()
	print(a)
	
	
with open('test.txt','r',encoding='utf-8') as fi:
	a=fi.read()
	print(a)