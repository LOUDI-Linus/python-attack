"""
@file:   3.抛出异常
@author: linuxzhen520@163.com
@date:   2020/04/10
@desc:


# 数字型数字
# 字符串 => 由0~9组成的数字
int('a')  => 如果我给的参数不符合它的要求 => 抛出异常 => ValueError: invalid literal for int() with base 10: 'a' => 中断
          => 提示 print("您的数据不符合要求") => 程序不中断
分析 => int函数 => 选择的是 => 抛出异常

a = myint('a')
b = myint('1')

print(a+b)
"""

# def myint(n):
#     """int的功能一致 -> n不合法 -> print"""
#     # isinstance => 判断n是不是指定的数据类型
#     if isinstance(n, int) or isinstance(n, float):
#         return int(n)
#     elif isinstance(n, str) and n.isdigit():
#         return int(n)
#     else:
#         print("您输入的数据不合法")
#
#
#
# a = myint('a')
# b = myint('1')
# # a -> None , b -> 1
# print(a, b)
# print(a+b)
# => TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# 如果用print给予提示，在类型转换一步虽然没有报错，但是由于数据的问题
# 后面的运算还是有可能会出错，运算出的结果跟预期不相符的
# 让它后面的运算过程中自然因为否种原因出错会更好，还是转换的过程抛出错误会更好
# => 方便定位问题！！

# 如果参数给得不对，给它返回一个合情合理的默认值。
# a = {1:1, 2:2}
# a.get(1) => 1
# a.get(3, default=0) => None
# web开发 -> 20条数据 -> per_page=n
# 客户端传送参数 args 给服务端
# args ={per_page:10}  => 服务端返回10条数据
# args ={} => args.get(per_page, 15) => 默认返回15条数据



# 当用户给的数据不对
# 1. 抛出异常
# 2. 给默认值处理 => 记日志



################################################################
# # 两种处理方式
# # 抛出异常
# def grade(score):
#     """
#     :param score: 给我传入一个分数
#     :return: 返回ABCD等级
#     """
#     if isinstance(score, str) and score.isdigit():
#         score = float(score)
#     if (isinstance(score, int) or isinstance(score, float)) and 0<= score <=100:
#         if score >=90:
#             return "A"
#         elif score >=70:
#             return "B"
#         elif score >=60:
#             return "C"
#         else:
#             return "D"
#     else:
#         # 抛出异常 => 关键字 raise 错误类型(提示参数)
#         raise ValueError("参数必须是[0~100]之间的整数或浮点数")
# # print(grade(97))
# # print(grade('abc'))
# # print(grade(120))
# print(grade('89'))
#
# 定义函数,如果函数是存在不合法的地方.raise


# while+print
# def grade(score):
#     """
#     不要在函数中写input,而是通过传参的方式将数据给函数
#     """
#     if score >=90:
#         return "A"
#     elif score >=70:
#         return "B"
#     elif score >=60:
#         return "C"
#     else:
#         return "D"
#
#
# while True:
#     score = input("请输入成绩")
#     if not score.isdigit():
#         print("参数必须是[0~100]之间的整数或浮点数")
#     else:
#         score = float(score)
#         if score > 100 or score < 0:
#             print("参数必须是[0~100]之间的整数或浮点数")
#         else:
#             break
#
# print(grade(score))



a = input("请输入一个整数")
if a.isdigit():
    int(a)
else:
    print("不合法")

try:
    a = input("请输入一个整数")
    int(a)
except:
    print("不合法")