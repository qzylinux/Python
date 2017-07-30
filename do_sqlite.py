#!/usr/bin/env python3

'SQLite'

__author__='qzy'

import sqlite3
#和数据库‘test.db’建立连接，如果‘test.db’不存在，新建数据库‘test.db’
sq=sqlite3.connect('test.db')
#操作数据库需要一个游标cursor
cur=sq.cursor()
#在数据库test.db中新建一个表，命名为mydb，表格的属性有id (整形，主键),name (可变长度的字符不大于20)，score(整形)
cur.execute('create table mydb(id int primary key, name varchar(20),score int)')

#在表格mydb中插入一条记录
cur.execute('insert into mydb (id,name,score)values(1,\'qzy\',90)')
#加入r之后后序不需要考虑转义操作，因为语句中有单引号，所以最外面的改为双引号
cur.execute(r"insert into mydb (id,name,score) values (2,'zhi',100)")
cur.execute(r"insert into mydb (id,name,score) values (3,'yuan',80)")
cur.execute(r"insert into mydb (id,name,score) values (4,'li',90),(5,'ling',88),(6,'ting',60)")

print(cur.rowcount)
#用完之后一定要关闭cursor
cur.close()
#提交事物
sq.commit()
#关闭对数据库的连接
sq.close()


sq=sqlite3.connect('test.db')

cur2=sq.cursor()

#根据条件where（score between ? and  ?是找到在？？之间的数据）返回记录的id,name，并按id排序
cur2.execute('select id,name from mydb where score between ? and  ? order by id',(90,100))
#通过fetchall获得上面select得到的结果集，返回的结果是一个list，每个记录是一个tuple
value=cur2.fetchall()

print(value)

cur2.close()
sq.close()
