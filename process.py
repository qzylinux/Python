#!/usr/bin/env python3

'multiprocessing-process'

__author__='qzy'

from multiprocessing  import Process
import os

def run_ch(name):
	print('the child process %s ID is %d.'%(name,os.getpid()))
#使用'''   '''来批量注释

if __name__=='__main__':
	print('parent %d is run.'%os.getpid())
	p=Process(target=run_ch,args=('test',))
	p.start()
	p.join()
	print('child process is end.')

	
	
#**********批量创建子进程*************************
from  multiprocessing import Pool
import os, time , random

def time_task(name):
	print('run task %s...'%name)
	start=time.time()
	time.sleep(random.random())
	stop=time.time()
	print('child process %s(id:%d) runs %0.2f seconds.'%(name,os.getpid(),stop-start))
	
if __name__=='__main__':
	print('parent id:%d'%os.getpid())
	Po=Pool(2)
	for i in range(3):
		Po.apply_async(time_task,args=(i,))
	print('waiting all process done....')
	Po.close()
	Po.join()
	print('All subproceses done.')
	
	
	
#***************子进程******************************************************
# 子进程有时候是外部进程
# 控制子进程的输入输出用subprocess模块  import subprocess


#*********************进程间通信*********************************
#queue

from multiprocessing import Process,Queue
import os, time, random

#子进程写如队列
def qu_write(q):
	print('process %d is write.'%os.getpid())
	for i in ['a','b','c']:
		print('put %s to queue..'%i)
		#写入队列
		q.put(i)
		time.sleep(random.random())
#读数据进程执行代码
def queue_read(q):
	print('process %d is read.'%os.getpid())
	while True:
		#从队列中读
		value=q.get(True)
		print('Get %s from queue.'%value)
		
if __name__=='__main__':
	print('parent id is %d'%os.getpid())
	#父进程创建Queue,并作为参数传递给子进程
	q=Queue()
	p1=Process(target=qu_write,args=(q,))
	p2=Process(target=queue_read,args=(q,))
	#启动子进程
	p1.start()
	p2.start()
	#等待子进程结束
	p1.join()
	#子进程2死循环，强制终止
	p2.terminate()