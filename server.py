#!/usr/bin/env python3

'server'

__author__='qzy'

import socket,threading
#socket模块的socket函数建立套接字，参数1说明使用IPV4，参数2说明是面向流的TCP协议
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定服务器的IP地址和端口号，方便客户端访问
s.bind(('127.0.0.1',9999))
#监听端口，允许最大等待接入数为5
s.listen(5)
print('waiting for connect...')

def tcplink(sock,addr):
	print('accept new socket from %s:%s'%addr)
	sock.send(b'welcome!')
	while True:
		data=sock.recv(1024)
		if not data or data.decode('utf-8')=='exit':
			break
		sock.send(b'Hello,%s!'%data.decode('utf-8').encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.'%addr)
	
while True:
	sock,addr=s.accept()
	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()
	
