"""
@file: 3.函数的返回值
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/19
@decs

"""
# packing => 打包 => 把多个数据放到一起
# unpacking => 解包 => 把多个数据让不同的变量接收
c=(1, 2, 3, 4, 5, 6)
a, *b = c
print(a,b)