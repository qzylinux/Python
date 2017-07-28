#!/usr/bin/env python3


'process_master.py'

__author__='qzy'

from multiprocessing.managers  import BaseManager
import time,queue
#新建两个队列，分别存放任务和任务结果
task_queue=queue.Queue()
result_queue=queue.Queue()
#从BaseManager类继承
class ManagerQueue(BaseManager):
	pass
#为了在win系统下匹配register的参数callable而新建的函数
#返回任务queue
def task_q():
	return task_queue
#返回结果queue
def result_q():
	return result_queue
	
#把两个Queue注册到网络上，第一个参数是自己设定的队列别名，为了区分不同的Queue的网络调用接口，callable参数关联了queue对象
ManagerQueue.register('get_task_queue',callable=task_q)
ManagerQueue.register('get_result_queue',callable=result_q)
#绑定IP地址和端口，验证码是‘123’,此处是主机，所以IP为本地地址
#authkey是为了保证通信不受其他机器干扰，主从机的authkey要一致
master=ManagerQueue(address=('127.0.0.1',5000),authkey=b'123')
#在win下运行
if __name__=='__main__':
	#启动Queue
	master.start()
	#通过网络访问Queue，而不是直接使用task_queue/result_queue这个队列访问
	task=master.get_task_queue()
	result=master.get_result_queue()
	#把任务放入队列
	task.put(10)

	print('try get result....')
	#等待结果队列
	value=result.get(True)
	print('result is %d'%value)
    #关闭队列
	master.shutdown()
	print('master end...')