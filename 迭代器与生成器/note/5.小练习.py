"""
@file:   5.小练习
@author: linuxzhen520@163.com
@date:   2020/05/07
@desc:
"""


# import string
# import random
# # 创建一个文件，内容随机字符串
# with open('big2.data', 'w+', encoding="utf-8") as f:
#     # f.write('aaaaaaaaaaaaaaaaaa\n'*10**7)
#     for i in range(10**7):
#         f.write(("".join(random.choices(string.ascii_lowercase, k=random.randint(1,50)))+"\n"))

# cpu消耗？ 多   => range, choices, randint, join，内存申请，内存释放
# 内存消耗？ 少  => 临时产生 -> 回收
# 一些些磁盘消耗


# 如果只是打开big.data文件 => 不会造成很大的内存消耗
# 什么情况下产生大的开销
# f对象是一个迭代器 => 保存当前状态及计算方法
with open('miui_HM6_9.9.3_da134d01c5_9.0.zip', 'rb+') as f:
    # for line in f:
    #     pass
    print(f, dir(f))

# windows中打开文件 => 会直接加载所有数据
# 多进程多线程 =>

"""
# fpath => 10G 

def read_file(fpath):
    "读取文件的内容并返回"
    with open(fpath, 'rb') as f:
         return f.read()
# f.read() => 将整个文件读取出来 => 10G
# next(f) => \n


def read_file(fpath):
    "读取文件的内容并返回"
    with open(fpath, 'rb') as f:
         while True:
             block = f.read(1024)
             if block:
                 return block
             else:
                 return 
# 不可行 => 
# read_file(a.txt) => 0-1024
# read_file(a.txt) => 0-1024


def read_file(fpath):
    "读取文件的内容并返回"
    with open(fpath, 'rb') as f:
         while True:
             block = f.read(1024)
             if block:
                 yield block
             else:
                 return 

f = read_file(fpath)
data = next(f)


打开的文件本身是迭代器 => 如果一个文件是文件文件（行长度不长）=>不需要自己写生成器函数
f = open(fpath)
data = next(f)
"""

# 当遇到程序运行得很慢 => 数据量、计算量大 => 迭代器/生成器
# 如果处理的数据非常大（1w+） => 迭代器/生成器

# 面试
# 可迭代对象和迭代器的区别？
# （可迭代对象 __iter__, 可迭代对象 => iter() => 迭代器）
#  实战 => 各自的优缺点+应用场景
#       => 可迭代对象（list,tuple,dict,set）: 可以随机取值，不适合大量的数据
#       => 迭代器（生成器表达式、生成函数）：只能迭代一次，从前往后next取值，数据状态不会造成很大的cpu和mem的瞬间占用
#                                         lazily produce => 惰性求值
#                                         某次在某种情况下.....使用迭代器.....性能提升


# 迭代器和生成器的区别？
# 生成器是一种特殊的迭代器
# 迭代器 => 定义一个类 => 自己去实现__iter__, __next__
# 生成器 => 生成器函数，生成器表达式