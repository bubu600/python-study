#！/usr/bin/env python
# coding=utf-8
# @Time    : 2019/10/4 12:37
# @Author  : Xiaojing
# @Email   : xiao-jing@msn.com
# @File    : test.py
# @Software: PyCharm

print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(21013))
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print('%d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Age: %s. Gender: %s' % (25,True))
