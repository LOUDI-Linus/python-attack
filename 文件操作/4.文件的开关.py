"""
@file: 4.文件的开关
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/23
@decs

"""
# 关闭语句--with语句,忘记，异常不管什么情况都能确保关闭，下列是打开了两个文件
with open('gbk.txt',encoding='gbk') as f,\
        open('test.txt',encoding='utf8') as f2:
    # with语句中操作---退出with语句块之后，文件会被关闭,
    print(f.read(),f2.read())
print(f.closed,f2.closed)   # True代表关闭

f1 = open('gbk.txt',encoding='gbk')
print(f1.read())
f1.close()
print(f1.closed)