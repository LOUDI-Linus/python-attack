"""
@file:   4.在函数中异常处理
@author: linuxzhen520@163.com
@date:   2020/04/10
@desc:
"""

# def task():
#     try:
#         1/0
#     except ValueError as ex:
#         print('error',ex)
#     finally:
#         print("always")
#     # 发现有一个异常
#     return "ok"
# # task()
# print(task())
# """
# always
# Traceback (most recent call last):
#   File "4.在函数中异常处理.py", line 17, in <module>
#     print(task())
#   File "4.在函数中异常处理.py", line 10, in task
#     1/0
# ZeroDivisionError: division by zero
#
# 执行过程
# 1. 调用函数
# 2. 1/0 => ZeroDivisionError
#    except => 没有捕获到错误
#    finally =>  打印always
# 3. 退出try...except异常捕获语句 => 有一个ZeroDivisionError错误没有被成功捕获处理
# 4. 异常退出 => 发生错误
#
# 打印always
# 打印Traceback
# """

# ############## 注意:如果在finally中使用return, 会导致traceback丢失
# def task():
#     try:
#         1/0
#     except ValueError as ex:
#         print('error',ex)
#     finally:
#         print("always")
#         return "ok2"
#     return "ok"
#
# print(task())
#
# """
# always
# ok2
#
# 1. 没有了traceback
# 2. 返回值是 ok2
#
# 为什么finally中使用了return之后, traceback就丢失了呢?
# traceback的信息被ok2取代了,函数直接返回了.
# """


def task():
    try:
        1/0
    except Exception as ex:
        print("error", ex)
        return "except"  # except是函数的返回值
    else:
        return "else"
    finally:
        print("finally")
        return "finally2"
    return "ok"


print(task())
"""
函数中的return => 退出函数 => 返回一个值
如果在except中使用了return  => 不直接返回 => finally
except

如果try/else/except中有return => 先去执行finally => 返回刚刚的return值
如果try/else/except中有return => 先去执行finally + return => 返回finally的return的值
"""
