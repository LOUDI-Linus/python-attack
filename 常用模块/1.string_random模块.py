"""
@file: 1.string模块
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/24
@decs

了解功能特性 -> 学习如何使用 -> 查看源码 -> 改进源码
"""
import string, random

# num = int(input("请输入指定字符串长度: "))
# # k表示指定长度
# rand_digits = "".join(random.choices(string.digits, k=num))
# rand_letters = "".join(random.choices(string.ascii_letters, k=num))



""""  random模块      """

# 随机生成0-1范围浮点数，以及自定义浮点数范围，不包含两边
print(random.random())
print(random.uniform(1,2))

# 随机产生范围内的整数,包含两边
print(random.randint(1,5))


#  返回指定递增基数集合中的随机数
print(random.randrange(2,10,2))

# 打乱序列中的所有元素(对元素自身做修改（必须是改变对象）)
list1 = [i for i in range(10)]
list2 = list(range(10,20))
str2 = "asdasdasd"
tuple1=(1,2,3,4,5,6)
random.shuffle(list1)
print(list1)

# 从序列中随机产生一个数据
print(random.choice(list1),type(random.choice(list1)))
# 产生k个数据,返回值为列表, 可用下标取值，字符串，列表元组-----hoices可以抽取重复的数据,既一个数据可以被抽取几次
print(random.choices(list1, k=3),type(random.choices(list1, k=3)))
# print(str2[1])
# print(tuple1[2])


# sample 抽取的元素不可重复,k值不能超过对象的长度，其他等同于choices
print(random.sample(list1,k=9))
