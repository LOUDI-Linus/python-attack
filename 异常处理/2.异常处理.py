"""
@file:   2.异常处理
@author: linuxzhen520@163.com
@date:   2020/04/10
@desc:
"""

# try:
#     a = float(input("请输入一个数据："))
#     b = float(input("请输入一个数据："))
#     print(a + b)
#
# except Exception as ex:
#     print(ex)
#     print("出错")



# try:
#     # 计算a和b的和
#     a = float(input("请输入一个数据："))
#     b = float(input("请输入一个数据："))
#     print(a+b)
# # 捕获所有的异常信息
# except:
#     print("运算过程出现错误！")
#
# print("不管怎么样，程序都会正常地执行！退出码0")


# try:
#     # 计算a和b的和
#     a = float(input("请输入一个数据："))
#     b = float(input("请输入一个数据："))
#     # ValueError
#     print(a+b)
# except ValueError as ex:
#     print(ex)
#     print("运算过程出现错误！")
#
# print("不管怎么样，程序都会正常地执行！退出码0")



# try:
#     # 计算a和b的和
#     a = float(input("请输入一个数据："))
#     b = float(input("请输入一个数据："))
#     # ValueError
#     print(a+b)
#     # 捕获Exception这种错误类型，也可以正常处理 => ValueError是Exception的子类
# # except Exception as ex:
# except ValueError as ex:
#     print(ex)
#     print("运算过程出现错误！")
#
# print("不管怎么样，程序都会正常地执行！退出码0")




#
# print("不管怎么样，程序都会正常地执行！退出码0")
"""
在try部分，发生任何错误都会去except匹配 =>
    except抓捕的NameError,现在发生的错误ValueError
在进行异常捕获时，注意错误类型匹配
    当前发生的错误 ==  except 错误类型          捕获-> 处理
    当前发生的错误 是  except 错误类型的子类    捕获-> 处理
如果没有匹配上错误类型，那么程序还是会异常退出。
"""



# # 多个Except分支，捕获不同的错误做不同的处理
# try:
#     # ValueError => 输入的数据不是int或float数字
#     a = float(input("请输入一个数据："))
#     b = float(input("请输入一个数据："))
#     print(a+b)
#     # ZeroDivisionError b输入的是0
#     print(a/b)
#     # ValueError
#     int('a')
#     x
# except ValueError as ex:
#     print(ex)
#     print("输入的数据必须是int或float的字符串！")
# except ZeroDivisionError as ex:
#     print("输入的除数不能为0")
# except Exception as ex:
#     print("出现了意料之外的错误")



# # 多个Except分支，捕获不同的错误做不同的处理
# try:
#     # ValueError => 输入的数据不是int或float数字
#     a = float(input("请输入一个数据："))
#     b = float(input("请输入一个数据："))
#     print(a+b)
#     # ZeroDivisionError b输入的是0
#     print(a/b)
#     # ValueError
#     # int('a')
#     x
# except Exception as ex:
#     print("出现了意料之外的错误")
# except ValueError as ex:
#     print(ex)
#     print("输入的数据必须是int或float的字符串！")
# except ZeroDivisionError as ex:
#     print("输入的除数不能为0")

"""
注意事项：
    如果将父类异常写在前面 的话，会吞噬所有的子类异常（子类异常的处理就没有意义 了）
    建议 => 先写最小的异常类，然后再写父类异常类
"""

#
# # else子句
# try:
#     # ValueError => 输入的数据不是int或float数字
#     a = float(input("请输入一个数据："))
#     b = float(input("请输入一个数据："))
#     print(a+b)
#     # ZeroDivisionError b输入的是0
#     print(a/b)
# except ValueError as ex:
#     print(ex)
#     print("输入的数据必须是int或float的字符串！")
# except ZeroDivisionError as ex:
#     print("输入的除数不能为0")
# except Exception as ex:
#     print("出现了意料之外的错误")
# else:
#     print("运行到这里，表示没有发生过异常哦~！")



# finally子句
# try:
#     # ValueError => 输入的数据不是int或float数字
#     a = float(input("请输入一个数据："))
#     b = float(input("请输入一个数据："))
#     print(a+b)
#     # ZeroDivisionError b输入的是0
#     print(a/b)
# except ValueError as ex:
#     print(ex)
#     print("输入的数据必须是int或float的字符串！")
# except ZeroDivisionError as ex:
#     print("输入的除数不能为0")
# except Exception as ex:
#     print("出现了意料之外的错误")
# else:
#     print("运行到这里，表示没有发生过异常哦~！")
# finally:
#     print("不管是否发生异常，都会执行这段代码")
# print("不管是否发生异常，都会执行这段代码11")


def grade(score):
    if isinstance(score, str) and score.isdigit():
        score = float(score)

    if isinstance(score, int) or isinstance(score, float) and 0<= score <= 100:
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        else:
            return "C"
    else:
        raise ValueError("参数必须是0~100的整数")


user = input("请输入: ")

print(grade(user))