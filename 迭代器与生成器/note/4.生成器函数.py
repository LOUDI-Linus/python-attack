"""
@file:   4.生成器函数
@author: linuxzhen520@163.com
@date:   2020/05/07
@desc:
"""

# # yield => 在函数中如果包含了yield => func1 生成器函数
# #       => 调用生成器函数的时候 => 创建一个生成器
#
# def func1():
#     a = 1
#     yield a
#     a += 1
#     yield a
#
# f = func1()
# print(f, type(f))
# # <generator object func1 at 0x0000018C43830350> <class 'generator'>
# print(f.__next__())
# print(f.__next__())
# # 生成器包含yield如何工作的？1. 保存状态 2. 返回数据
# # 当如果通过next(f), f.__next__(), f.send(None), f.send(n) => 触发执行生成器中代码
# # 从生成器中记录的上一次执行的位置开始执行，一直遇到yield关键字的时候，返回yield后面的表达式的值，保存当前的状态,不继续执行
# # 如果生成器内容执行完毕，或close => StopIteration


# send => 往生成器中发送数据

# def func1():
#     a = 1
#     data = yield a
#     print(1, data)
#     a += 1
#     data = yield a
#     print(2, data)
#
# f = func1()
# print(f, type(f))
# # <generator object func1 at 0x0000018C43830350> <class 'generator'>
# print(f.__next__())   # => next(f), f.send(None)
# # 1 , 保存状态（32,....）
# print(f.__next__())   # => next(f), f.send(None)
# # 1 None
# # 2
# print(f.__next__())  # => next(f), f.send(None)
# # 2 None
#
# # f2 = func1()
# # for i in f2:
# #     print(i)


# def func1():
#     a = 1
#     data = yield a
#     print(1, data)
#     a += 1
#     data = yield a
#     print(2, data)
#
# f = func1()
# # print(f, type(f))
# # <generator object func1 at 0x0000018C43830350> <class 'generator'>
# # 第一次必须f.send(None)
# print(f.send(None))
# # 1
# print(f.send(6))
# # 1 6
# # 2
# print(f.send(10))
# # 2 10
# # send的数据，发送到上一次执行的yield的位置


# yield from

g0 = (str(i) for i in range(10))
# '0','1','2','3'.....

def g1():
    yield g0


def g2():
    yield from g0

rg2 = g2()
print(next(rg2))
print(next(rg2))
print(next(rg2))
print(next(rg2))


# rg1 = g1()    # 创建了一个生成器
# rg10 = next(rg1)
# print(next(rg10))
# print(next(rg10))
# print(next(rg10))
# print(next(rg10))
# print(next(rg10))

# 返回g0

# yield 表达式      => 直接返回表达式的结果
# yield from 生成器 => 从生成器取结果，在生成器中遇到了yield，保存状态，停止


# b/s, c/s
