"""
@file: 3.函数传递参数
@author: Cooper.wy_zou1103@163.com
@date: 2021/03/25
@decs

"""
# 函数的传参本质上是传递的引用
def f(x):
    print(id(x))
    x = 100
    print(x)
    print(id(x))
# 不可变对象
a = 1
print(id(a))
f(a)
print(id(a))

print('\n')

# 传递的可变对象，有可能改变原对象
def f(x):
    print(id(x))
    x.append(100)
    print(id(x))
    print(x)

a = [1,2,3]
print(id(a))
f(a)
print(a)
print(id(a))


