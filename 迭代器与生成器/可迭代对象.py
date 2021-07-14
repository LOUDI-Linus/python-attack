"""
@file: 可迭代对象
@author: Cooper.wy_zou1103@163.com
@date: 2021/07/12
@decs

"""
# https://blog.csdn.net/LaoYuanPython/article/details/94362077  详细解答
# 一个对象实现了一个next与iter方法就是迭代器
from collections.abc import Iterable, Iterator
# def get_data():
#     a= [i for i in range(0,3)]
#     items = a.__iter__()
#     print(type(items))
#
# get_data()
a = [1,2,3]
# items = a.__iter__()
items = iter(a)
print(dir(items))
# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
print(items,type(items),isinstance(items,Iterable))

