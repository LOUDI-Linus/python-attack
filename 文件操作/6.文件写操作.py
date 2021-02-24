"""
@file: 6.文件写操作
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/23
@decs

"""
""" 
什么时候落盘？
1.脚本执行完毕，文件关闭
2.f.flush  强行将缓冲区的内容落盘
3. buffering=1 => (在text模式下) 当缓冲区遇到\n的时候，将缓冲区的内容写到文件
4. buffering=0 => （在二进制模式下） 实时写入
4. buffering=2 => (在text模式下) 2*4096 ,如果写入的数据超过缓冲区的大小，那么缓冲区的内容写入文件
                   f.write('a'*2*4096) + f.write('a')
"""

import time
with open('test.txt', mode='a+', encoding='utf8') as f,\
    open('utf8.txt',mode='rt+',encoding='utf8') as f2:
    f.write("\n测试1")
    f2.truncate(3)
    # f.flush()
    # time.sleep(5)

# f = open('test.txt',mode='a+',encoding='utf8')
# f.write('\nhello')
#
# print(f.closed)



