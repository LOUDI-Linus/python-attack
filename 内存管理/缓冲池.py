"""
@file: 缓冲池
@author: Cooper.wy_zou1103@163.com
@date: 2021/03/25
@decs

"""
# 字符串的intern机制
# python对于短小的，只含字母数字的字符串自动触发缓存机制(只是创造新的引用，而不是对象本身)，其他情况不会缓存
from sys import getrefcount

a= "hello "
print(id(a))

b="hello "
print(id(b))
print(a is b)
print(getrefcount(a))