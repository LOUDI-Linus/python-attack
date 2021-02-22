"""
@file: 6.变量的作用域
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/20
@decs

作用域，从被定义开始生效
"""
"""变量种类为局部(local)，全局(global)，内建变量(built-in)

命名空间  -> 记录变量
local namespace
global ---


变量的查找方式
L
E
G
B
"""
#内建
print(__name__)
print(__file__)   #路径
print(__doc__)    #著者信息

# 局部变量
# def func3(x):
#     print("x is ", x)
#     x = 2   #local 只在内部生效
#     print("change local x to ", x)
#
# x = 10
# func3(x)
# print("x is ", x)

# 全局变量--整个模块生效
# def func3():
#     # 此时的两个x是同一个x
#     print("x is ", x)
#
# x = 10
# func3()
# print("x is ", x)


# def func3():
#     global x   #声明使用全局变量
#     # local => x
#     # UnboundLocalError: local variable 'x' referenced before assignment
#     # 为什么会出错:因为func3这个local命名空间中有x,根据变量查找顺序,取local的x,
#     # 当它取x的值时,这时x还未定义
#     print("x is ", x)        #声明全局变量所以为10
#     x = 3    #此时全局变量变更为3
#
# # global => x
# x = 10
# func3()
# print("x is ", x)


# # __name__ = 1
# def func1():
#     """enclosing"""
#     # __name__ = 2
#     def func2():
#         """local"""
#         # __name__ = 3
#         a = 1
#         b = 2
#         print(__name__)
#         # 当前对象的命名空间变量
#         print(locals())
#         print(globals())
#     func2()
# func1()
# # # globals => 全局变量
# print(globals())
# # # locals => 本地变量
# # print(locals())
#
# # LEGB -> Name Error
# # 就近原则

#　global , nonlocal
# globals(), locals()

# nonlocal 关键字用于在嵌套函数内部使用变量，其中变量不应属于内部函数。
def func():
    x = 1
    def func2():
        nonlocal x   #使用
        # global x   # 使用全局变量x
        print("x is", x)
        x = 2
    func2()
    print('func',x)
x = 3
func()
print('global',x)