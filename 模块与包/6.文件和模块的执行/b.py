"""
@file:   b.py
@author: linuxzhen520@163.com
@date:   2020/04/09
@desc:
"""

import a

# 为什么不生成b.py
# 如果一个文件被当作模块导入, 表示这个模块经常要用的. 生成pyc文件
# b.py => 不是模块导入 => 这类文件,经常会做修改


# 在python3中pyc文件生成__pycache__目录
# 在python2中pyc文件生成到当前目录，文件名 => 源文件名.pyc