"""
@file: 1.function
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/03
@decs
函数就是带名字的代码块，可用于完成特定的工作
"""

# 简单定义一个函数
def great_user():
    """此处为文档字符串注释，说明此函数的功能"""
    print("hello")

# 调用函数
great_user()


# 向函数传递信息
def great_user(username):
    print("hello"+'\t'+username.title())

great_user("zwc")


""""形参与实参 
username是一个形参--函数完成其工作所需要的一项信息
zwc是一个实参--调用函数时传递给函数的信息
"""
