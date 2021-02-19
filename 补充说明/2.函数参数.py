"""
@file: 2.函数参数
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/19
@decs

"""

# name:str =>类型注释  表示name 期望得到的数据类型,但并不是强制要求
# ->   函数的返回值类型，函数没有return，则返回值默认为None
def stu_messgae(name:str, age:int) -> str:
    result = f"名字:{name}\n年龄:{age}"
    return result

user1=stu_messgae('zwc',1)
# 只有使用print进行输出，内容才会输出
print(user1)
