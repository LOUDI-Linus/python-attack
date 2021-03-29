"""
@file:   main
@author: linuxzhen520@163.com
@date:   2020/04/09
@desc:
"""

# a = 1
# print(dir(a))

# 测试一
#
# from code import model

# # 执行了哪些内容？
# # code.__init__.py 文件的内容
# # => 当我导入某个包时，自动执行这个包下面对应的__init__.py文件
# # code.model 文件的内容
#
# # 可以使用 => 如果一个模块导入了，那么它里面的所有内容都是可以用的！！
# #            但是，由于约定俗成规定，所以呢，如果看到一个对象_开头命名，不建议在外面使用
# print(model.a)
# print(model._a)
# print(model.__a)
# print(model.__a__)
# model._func()
# model.func()

# # 测试二
# # 如果使用通配符方式导入, 那么以_开头的对象都不会被导入
# from code.model import *
# print(a)
# func()
# # print(_a)
# # print(__a)
# # print(__a__)
# # _func()


# 测试三
# # 从包中使用import * 直接导入模块 => 无法导入
# from code import *
# print(model)
# print(_model)

# # 如何能让模块/包直接导入使用呢 ?  => __init__.py , __all__
# # __all__ = ['_model', 'model']
# from code import *
# print(model)
# print(_model)

# # 如何能让模块/包直接导入使用呢 ?  => __init__.py , __all__
# # __all__ = ['_model', 'model']
# # 在__init__中加入了一个test函数 => 不能用*导入
# from code import *
# print(model)
# print(_model)
# 可以这么用
# from code import test
# test()
# model.func()
#
#
# # 代码导入的优化 =>
# # from code.model import func
# from code import func
# func()
#

# # 每一个文件,都有一些内置属性, __name__, __file__
# print(__name__, __file__)
# from code import model
# # 当直接执行model.py文件 => __name__ => __main__
# # 当from code import model  => __name__ => code.model => 模块名
#

# 当导入函数的时候, => 测试代码直接就被运行了!!!

from code.mytime import str_to_datetime

#查看模块路径
import random
import json
print(random.__file__)
print(json.__file__)





