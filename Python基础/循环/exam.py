#！/usr/bin/env python
# coding=utf-8
# @Time    : 2019/10/4 16:59
# @Author  : Xiaojing
# @Email   : xiao-jing@msn.com
# @File    : exam.py
# @Software: PyCharm

sum = 0
for x in range(101):
    sum += x
print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print('Hello,%s!' % i)

n = 1
while n <=100:
    if n > 10:
        break
    print(n)
    n += 1
print('END')

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)