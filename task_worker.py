#!/usr/bin/env python3


'process_master.py'

__author__='qzy'

from  multiprocessing.managers  import BaseManager

#由于队列是存在于主机的，所以从机不需要新建管道

class QueueManager(BaseManager):
	pass
	
#由于QueueManager只能从网络上获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
#端口和authkey注意与主机一致
m=QueueManager(address=('127.0.0.1',5000),authkey=b'123')
#连接到服务器
m.connect()

task=m.get_task_queue()
result=m.get_result_queue()

value=task.get(True)

r=value*value

result.put(r)

print('worker exit...')