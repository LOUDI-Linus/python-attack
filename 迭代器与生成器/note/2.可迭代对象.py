"""
@file:   2.可迭代对象
@author: linuxzhen520@163.com
@date:   2020/05/06
@desc:

容器：把多个元素组织在一起的数据结构，in ，not in
可迭代对象：
    凡是可以返回一个迭代器的对象称之为可迭代对象（__iter__）
    对象实现: __iter__()
             __iter__()方法:返回一个迭代器
    查看：
        from collections.abc import Iterable
        print(isinstance('abc', Iterable))
        print(isinstance(1, Iterable))

    class A():
    pass

a = A()
print(dir(a))
from collections.abc import Iterable
print(isinstance(a, Iterable))

class A():
    def __iter__(self):
        pass

b = A()
print(dir(b))
from collections.abc import Iterable
print(isinstance(b, Iterable))


"""
# 迭代器
# 1. 将一个可迭代对象通过iter() => 获取迭代器
# 2. 只能通过next向后取值 ，不能通过下标随机取值
# 3. 迭代器是有类型的
# 4. 如何判断一个对象是不是迭代器
#    __iter__, __next__
#    isinstance(obj, Iterator)
# 5. 迭代器是有状态的   =>   内部会记录一些数据
# 6. 所有的迭代器都是可迭代对象


from collections.abc import Iterable, Iterator
x = [1, 2, 3]
print(x, type(x), isinstance(x, Iterable))

# x.__iter__() => 返回一个迭代器
y = x.__iter__()
z = iter(x)
print(y, type(y), isinstance(y, Iterable))

# 重点！！迭代器的特点 => 只能通过next向后取值 ，不能通过下标随机取值
# 取列表中的3 =>
print(x[2])
print(next(y))
print(y.__next__())
print(next(y))
print(next(z))

s = iter("abc")
print(s)
t = iter((1, 2, 3))
print(t)



# 生成无限序列
# 10~+
from itertools import count
counter = count(10)
print(counter, type(counter), isinstance(counter, Iterable), isinstance(counter, Iterator))
for i in range(10**10):
    print(next(counter))
# 迭代器的优点
# 迭代器是有状态的           =>   内部会记录一些数据 n=10
# 迭代器内部有一个计算规则   =>   n+=1
# 只有通过next取值的时候，才会去根据数据状态，计算出下一值 （不保存所有的数据，）
# 不能随机取值，不能返回取值
# 1T,2T 如果数据量特别大的时候，比较适合迭代器

# py2
x = range(10**6)
# <type 'list'> => 0.......10**6-1
# 好处：随机取值
# 缺点：数据量比较大 => MemeryError

# py3
y = range(10**20)
# range object => 类似迭代器
y = iter(y)
# 好处：数量巨大也没有关系
# 惰性求值 => 需要的时候再计算

dic = {1:1}
print(dic.keys())


# next方法如何实现
# next(obj) => obj.__next__() => obj.__next__()
# 定义类 => 实现/重写__next__
