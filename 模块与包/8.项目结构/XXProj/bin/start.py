"""
@file:   start.py
@author: linuxzhen520@163.com
@date:   2020/04/10
@desc:
"""

# from ..src import main

# 把XXProj目录添加成sources root实际上做了什么
# sys.path
import sys,os
# print(sys.path)
print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(__file__))

# 定义项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR1 = os.path.dirname(os.path.abspath(__file__))


print(BASE_DIR)
print(BASE_DIR1)
# 添加到环境变量 !!!!!
sys.path.append(BASE_DIR)
#
#
from src import main
# from conf import settings
main.run()


"""
把项目根目录添加到环境变量，导入的时候，从根目录开始导入
框架中基本上都是这样做的
"""


