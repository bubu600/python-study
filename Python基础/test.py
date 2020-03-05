#！/usr/bin/env python
# coding=utf-8
# @Time    : 2019/10/6 10:47
# @Author  : Xiaojing
# @Email   : xiao-jing@msn.com
# @File    : test.py
# @Software: PyCharm

# with open(r'D:\1.log','r',encoding='gbk', errors='ignore') as f:
#     #print(f.readlines())
#     for i in f.readlines():
#         print(i.strip())

# with open(r'D:\2.log','a',encoding='utf-8') as l:
# #     l.write('\nhello world')
# #
# # fpath = r'C:\Windows\system.ini'
# #
# # with open(fpath,'r') as f:
# #     print(f.read())

# from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world!')
#
# print(f.getvalue())

# from io import  StringIO
# f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

# import os
# print(os.name)
# print(os.environ)
# print(os.path.abspath('.'))
# print(os.path.join(os.path.abspath('.'),'testdir'))
# os.mkdir(r'D:\工作学习\python-study\Python基础\testdir')
# os.rmdir(r'D:\工作学习\python-study\Python基础\testdir')
# print(os.path.split(r'D:\工作学习\python-study\Python基础\file.txt'))
# print(os.path.splitext(r'D:\工作学习\python-study\Python基础\file.txt'))

# import pickle
# d = dict(name='Bob',age=20,socre=88)
# print(pickle.dumps(d))
#
# with open(r'D:\3.log','wb') as f:
#     pickle.dump(d,f)
#
# with open(r'D:\3.log','rb') as l:
#     print(pickle.load(l))

# import json
# d = dict(name='Bob',age=20,socre=88)
# print(json.dumps(d))
#
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str))
#
# class Student(object):
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# s = Student('Bob',20,88)
#
# def student2dict(std):
#     return {
#         'name':std.name,
#         'age':std.age,
#         'score':std.score
#     }
#
# print(json.dumps(s,default=student2dict))

import re
# test = '用户输入的字符串'
# if re.match(r'正则表达式', test):
#     print('ok')
# else:
#     print('failed')
#
# str1 = 'a b  c'
# str2 = 'a,b, c  d'
# str3 = 'a,b;; c  d'
# print(re.split(r'\s+', str1))
# print(re.split(r'[\s\,]+', str2))
# print(re.split(r'[\s\,\;]+', str3))
#
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-123456')
# print(m)
# print(m.groups())
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
#
#
# def is_valid_email(addr):
#     if re.match(r'^([\d\w\.]*)\@(.*)\.(.*)$', addr):
#         return True
#     else:
#         return False
#
# # 测试:
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')

# def name_of_email(addr):
#     m = re.match(r'^(.*)@(.*)$', addr)
#     a = re.split(r'[\>]',m.group(1))
#     return a[0].strip('<')
#
#
# assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
# assert name_of_email('tom@voyager.org') == 'tom'
#
# print('ok')
#
# import time
# print(time.time())

# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
#
# import hashlib
#
# def login(user, password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     passwd_md5 = md5.hexdigest()
#     db_md5 = db[user]
#     print(passwd_md5,db_md5)
#     if passwd_md5 == db_md5:
#         return True
#     else:
#         return False
#
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')

# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         print(data)
#
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         print('&%s;' % name)
#
#     def handle_charref(self, name):
#         print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')


from turtle import *

# 设置色彩模式是RGB:
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

speed("fastest")

draw_tree(l, 4)

done()