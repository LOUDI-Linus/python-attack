"""
@file: 1.文件的理解
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/22
@decs
文件的两种格式
        文本与二进制(是存储的内容（二进制/字节码）)
        内存磁盘都是二进制文件，查看需要转换
        文件读取分为t模式与b模式

encode编码可指定任何合适的编码方式，decode解码，一定需要对应的编码方式
编码可以解决人与计算的沟通问题
"""

# t模式
f = open('test.txt',  'rt+', encoding='utf-8')
print(f.read())
# f.write("world")


#b模式
f2 = open('test.txt',  'rb')
# print(f2.read())
content = f2.read()
print(content,content.decode("utf-8"))   # 解码

