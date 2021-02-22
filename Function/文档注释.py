"""
@file: 文档注释
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/22
@decs

"""
def message():
    """这是一个样例"""
    print("hello world")

print(__doc__)
print(message.__doc__)
help(message)
