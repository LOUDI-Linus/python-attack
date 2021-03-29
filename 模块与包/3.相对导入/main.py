"""
@file:   main
@author: linuxzhen520@163.com
@date:   2020/04/09
@desc:

什么是相对导入呢？
    Linux相对路径 . , .. => 相对当前目录
    相对当前目录进行导入

使用.和..来进行导入

要求：
1. 只能导入【包】中的模块/子包
2. python会自动识别一个目录是不是一个包
3. 相对于当前被执行的文件而言
    a. 当前执行的文件所在的目录（及上层目录）不是一个包
    b. 子目录及子子目录都是包
4.识别.或者..代表的目录是不是一个包
"""

# # 可以导入。当前这不是相对导入 => 绝对导入 => 根据 PATH 导入
# import example
# example.show()
# import sys
# print(sys.path)

# 这是一个相对导入 -> .和..一定要代表一个包
# . => 3.相对导入 => 不是一个包
# from . import example
# ImportError: attempted relative import with no known parent package

from pack01 import one
one.fun1()

"""
from pack01 import one
# one.py -> . => pack01 -> 是一个包
from . import two
# two.py
print("i am pack01.two")

def fun1():
    print("pack01.two.func1")

"""


