#！/usr/bin/env python
# coding=utf-8
# @Time    : 2019/10/4 17:07
# @Author  : Xiaojing
# @Email   : xiao-jing@msn.com
# @File    : test.py
# @Software: PyCharm

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#判读值是否在字典中
'Thomas' in d
d.get('Thomas',-1)

s1 = set([1,2,3])

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
f = calc_sum(1,2,3,4)
print(f)

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f1 = lazy_sum(1,2,3,4,5)
f2 = lazy_sum(1,2,3,4,5)
print(id(f1))
print(id(f2))

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1 = count()[1]
print(f1())


gcount = 0

def global_test():
    gcount += 1
    print (gcount)
global_test()
