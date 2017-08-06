#!/usr/bin/env python3

'process sensordata'

__author__='qzy'

buffer=[]
#datali=[]
with open('onlydata.txt','r') as f:
	while True:
		lines=f.readlines()
		for line in lines:
			line=line.strip('[]\n')
			buffer.append(line)
		else:
			break
	#print(buffer)
	#length=len(buffer)
	#print(length)
	#datali=buffer[0:2]
	data=','.join(buffer)
	#print(data)
	with open('data.txt','w') as fi:
		fi.write(data)