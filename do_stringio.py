#!/usr/bin/env python3
# encoding utf-8

'StringIO test'

__author__='qzy'

#StringIo和ByteIO是对内存的读写
from io import StringIO

fi=StringIO()
fi.write('hello,world!')
print(fi.getvalue())

from io import BytesIO

fi=BytesIO()
fi.write('abc'.encode('utf-8'))
print(fi.getvalue())
print(fi.read())

fi=BytesIO('abc'.encode('utf-8'))
print(fi.read())