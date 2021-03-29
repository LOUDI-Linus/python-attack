import json
import sys
import os

print(json)
print(sys)
print(os)
# 在标准库中。
# 分类 => 重要的内置模块sys, math, os   => 不管path中否能有同名的模块
#         json不那么重要的模块

# sys.path的第一个目录，通常是当前目录
print(sys.path)

"""
导入包的两种方式。
相对导入。多层目录层级项目中用

绝对导入。
导入查找顺序问题？
1. 比较重要的内置模块sys, math, os 优先级高
2. sys.path => Python的环境变量
   按照sys.path输出的列表给出的目录，依次去查找
   如果找到了，直接返回
   如果没有找到，继续往后查找
3. 如果两个都没有找到，ModuleNotFoundError: No module named 'kkk'


"""
# print(sys.path)
# sys.path.append('C:')