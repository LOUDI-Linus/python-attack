# """
# @file:   3.生成器
# @author: linuxzhen520@163.com
# @date:   2020/05/07
# @desc:
# """
# # 生成器是特殊的迭代器
# # 生成器表达式
# # 生成器函数 => 定义了一个函数，在这个函数中有yield关键字
#
# #
# # def func1():
# #     x = 8
# #     return x-1
# #     y = 6
# #     return y+2
# #     z = 3
# #     return z
# #
# # f = func1()
# # print(type(func1), f)
# # # <class 'function'> 7
#
# # 生成器函数 => 调用该函数会创建一个生成器
# def func1():
#     x = 8
#     yield x-1
#     y = 6
#     yield y+2
#     z = 3
#     yield z
#
# # func1() => 创建一个生成器generator
# f = func1()
# print(type(func1), f)
# # <class 'function'> <generator object func1 at 0x000001F4B97A0350>
# print(dir(f))
# # f 是一个生成器 => __iter__, __next__
#
# print(next(f))
# # 当遇到yeild时，返回yield后面的表达式的值，同时保存当前的状态（x=8,运行到了line2）
# print(next(f))
# # 从lin3开始继续往后执行当遇到yeild时，返回yield后面的表达式的值，同时保存当前的状态（x=8,y=6运行到了line4）
# print(next(f))
# # print(next(f))
# # StopIteration
#
#
# # 实现无限大fib数列 => 利用生成器函数（迭代器）
# def hanshu():
#     # a第一项，b第二项
#     a=1
#     b=1
#     while True:
#         # 返回第n项的值
#         yield a
#         # a,b = 1,2
#         a,b = b,a+b
#         # c=a
#         # a=b
#         # b=a+c
# f=hanshu()
#
# # print(next(f))
# # print(next(f))
# # for i in f:
# #     # 隐式地调用next(f)
# #     print(i)
# #     if i>30:
# #         break
#
# # 那老师我想取到第7项 咋操作
# # for i in range(7):
# #     print(next(f))
#
# result = [next(f) for i in range(7)]
# print(result)
#
#
# #
# # # send => 往生成器中发送一些数据，达到与生成器交互的目的
# def counter(start_at=0):
#     count = start_at
#     while True:
#         val = yield count
#         if val is not None:
#             count = val
#         else:
#             count += 1
#
# count = counter(5)
# # TypeError: can't send non-None value to a just-started generator
# # 第一次必须count.send(None)或next(count)
# # print(count.send(1))
# print(count.send(None)) # next(count)
#
# """
# line 85 yeild count
# line 85 val = 1
# """
#
#
# print(count.send(1))       #  1
# print(count.send(None))    #  2
# print(next(count))         #  3
#
# print(count.send(100))     #  100
# print(count.send(None))    #  101
# print(next(count))         #  102
#
# count.close()
# print(next(count))
# # StopIteration


# yield from
def gen(x):
    i = 0
    while i<x:
        yield i
        i += 1

def g1(x):
    # yield直接返回表达式的结果
    yield gen(x)

def g2(x):
    # yield from 运行后面的生成器，在生成器中遇到了yield，保存状态，停止
    yield from gen(x)

g = g2(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))