"""
@file: 4.匿名函数
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/20
@decs
应用场景---不会被重复使用，功能简单，能用一个简单的表达式实现
"""
list1 = [i for i in range(1,11)]
list2 = [a for a in range(20,31)]

# lambda匿名函数，以及map函数(高阶函数)的用法--将可迭代对象中的每一个元素交给func执行一次
print(list(map(lambda x:x*2,list1)))
print(list(map(lambda x,y:x+y,list1,list2)))

func1 = lambda a,b:a+b
print(func1(1,2))
help(lambda :110)

# lambda也允许有默认值和使用变长参数
func2 = lambda *a:a
func3 = lambda x,y=2:x+y
print(func2(1,2,3))
print(func3(1))