#！/usr/bin/env python
# coding=utf-8
# @Time    : 2019/10/4 16:50
# @Author  : Xiaojing
# @Email   : xiao-jing@msn.com
# @File    : exam.py
# @Software: PyCharm

height = 1.75
weight = 80.5

bmi = weight/(height**2)
if bmi > 32:
    print('严重肥胖，bmi %.2f' % bmi)
elif 28 < bmi <= 32:
    print('肥胖，bmi %.2f' % bmi)
elif 25 < bmi <= 28:
    print('过胖，bmi %.2f' % bmi)
elif 18.5 < bmi <= 25:
    print('正常，bmi %.2f' % bmi)
else:
    print('过轻 bmi %.2f' % bmi)