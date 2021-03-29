"""
@file:   main
@author: linuxzhen520@163.com
@date:   2020/04/09
@desc:
"""

import math
# 如果看到一个python的标准库，函数的内容是pass =>
# 这部分功能实现是c代码实现的，math.py 只是用来给我们看一下功能，帮助

print(math.sqrt(4))

# 模块和包本身是没有功能的，只是代码组织形式。
# 真正调用的是 => 函数(def)/变量/类(class)
# 模块.函数
# 模块.变量
# 模块.类
# 包.模块.函数

import chardet
# 点击源代码 => chardet/__init__.py => 包

# 用法一：
print(chardet.enums.InputState)
# 用法二：可以直接使用__init__.py中定义或导入的内容
# 对于常用的内容，可以直接在__init__.py文件中导入，然后直接使用
print(chardet.detect)

################################################################

# 直接导入我们需要的对象
from math import acos
print(acos(1))

from chardet.enums import InputState
print(InputState)

from chardet import enums
print(enums.InputState)
# 使用的是，import出来的对象

# 导入math模块下所有的内容 => 个人不推荐这种导入方式
from math import *
# 推荐：导入需要的两个函数 => 按需导入
from math import sqrt, acos

"""
a.py => sqrt

from a import *
from math import *

# 自己想用a -> sqrt 
sqrt() # math中sqrt

# 不清楚
"""


modname = input("请输入你要导入的模块名：")
print(modname)

# 导入modname这个模块
# import modname

# 根据模块名字符串导入模块(推荐！！)
# mod = __import__(modname)
# print(dir(mod), mod)

import sys
import os
"""
sys/os模块标准库 => 遇到自定义模块与这些模块名重复

<module 'sys' (built-in)  => 功能实现是由C代码完成
<module 'os' from 'C:\\Python38\\lib\\os.py'>
"""


import importlib
mod = importlib.import_module(modname)
print(dir(mod), mod)