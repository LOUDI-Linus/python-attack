"""
@file: 5.文件的基本操作
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/23
@decs
读取文件的三种方式read，readlines,readline
"""
#
# import chardet
# with open('gbk.txt',encoding='gbk') as f:
#     print(f.tell())   # 光标位置，gbk1汉字=2字节
#     print(f.read(2))  # 读取n个字符
#     print(f.tell())   # 光标位置，gbk1汉字=2字节
#
#     # 移动光标：参数1为移动量(单位量为字节) ，参数2为相对哪来移动（0-开始位置，1-当前位置(只能在b模式中使用，2也是)，2-末尾）
#     f.seek(2,0)  # 会读取光标之后的字符
#
#     print(f.tell())
#     print(f.read(1))
#     # # f => 可迭代对象 => for取，每一次取到一行数据
#     # for i in f:
#     #     print(i)
#
#     f.seek(0,0)
#     # f.readline => 从当前位置读取一行信息（\n） => 返回一个str
#     print(f.readline(),end="")  # 取消换行
#     print(f.readline())
#
#     f.seek(0,0)
#     # f.readlines => 返回从当前位置到文件末尾 => 返回一个列表
#     print(f.readlines())
#
#  # 退出with语句块时，文件被关闭， 查看f是否关闭
# print(f.closed)


with open('test.txt','rb') as f2:
    # 读取前五行
    for i in range(5):
        print(f2.readline())
    print('\n')
    f2.seek(0,0)
    # 读取全部
    print(f2.read().decode('utf-8'))

    # 后12个字节
    print('\n')
    f2.seek(-12,2)
    print(f2.tell())
    print(f2.read().decode('utf-8'))



