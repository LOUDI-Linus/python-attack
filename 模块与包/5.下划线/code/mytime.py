"""
@file:   mytime
@author: linuxzhen520@163.com
@date:   2020/04/09
@desc:
    编写模块的时候,需要测试
    在一个模块中,通常包含两个部分的内容(完成的功能(函数), 测试代码)
"""

def str_to_datetime(yourstr:str):
    print(f"{yourstr}这是一个将时间字符串转换成时间时间格式的函数")

if __name__ == "__main__":
    """
    如果我当前直接运行这个文件,那么就执行测试代码,否则就不执行测试代码
    当编写模块的时候,测试代码通常就写在这里
    """
    str_to_datetime("20200409")
    str_to_datetime("2020409")
else:
    print("我是被当作模块导入的,所以不执行测试代码~")

