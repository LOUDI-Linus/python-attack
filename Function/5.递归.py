"""
@file: 5.递归
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/20
@decs

"""
# n! = 1*2*3*4...*n
def func(n):
    if n == 1:
        return 1
    return n*func(n-1)

print(func(4))

"""     斐波拉契数列，某项的值等于前两项的和      
F(1)=1
F(2)=1
F(n)=F(n - 1)+F(n - 2)（n ≥ 3，n ∈ N*）
"""

def func1(n):
    if n == 1 or n == 2:
        return 1
    return func1(n-1)+func1(n-2)

# 函数是可以嵌套的