"""
@file: 1.字符串的常见方法
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/19
@decs

"""
#查看字符串的方法
print(dir(str))

#查看某个方法的具体使用
help(str.count)
"""
 S.count(sub[, start[, end]]) -> int
 [] ： 表示这是一个可选项
 <> : 表示必填项
 -> int : 这个函数/方法的返回结果是一个int类型
"""


# replace :将查找到的指定字符替换成另外一个字符,默认会所有的都替换
message = "hello Hlol Hello hello"
print(message.replace("o", "0"))
print(message.replace("o", "0", 2))

# split => 切割 用指定的分割符切割字符串, 默认用空格切割 =>list，需要完全匹配
message = "root:x:1:this is root:/bin/bash"
result = message.split(':')
print(result, result[3])



"""     字符串拼接       """
# +号拼接

# join拼接
result1="".join(result)
print(result1)

# % => 字符串拼接、字符串格式化
str1 = "hello"
str2 = "world"
# %s => 表示这里会有一个数据 => %() 中会有一个数据与之对应
# %s的数量与数据的数量必须一致，否则 => TypeError: not enough arguments for format string
result3 = "%s %s" %(str1, str2)
print(result3, type(result3))
# %s => s表示什么意思呢？s => str


# %的格式功能（对齐(+右对齐，-左对齐)，宽度 10）
print("%-10s" %str1)
print("%+10s" %str1)


## format   python2.几开始支持        推荐！！！！！！！！！！！！！
# 默认情况下，format的参数依次放到{}中, 如果提供的参数有多余的(a) ，不会出错
str3 = 'Good'
str4 = 'luck'
# 每个参数str1,str2都有一个序号第一个0， 第二个1.....     好处之一~~~~
result4 = "{1}{0}".format(str3, str4)
print(result4,type(result4))

username = 'zwc'
age = 18
my_message = "My name is {name}, age is {age}".format(age=age, name=username)
print(my_message)


## f   python3.5之后才支持使用
result4 = f"{str3}{str4}"
print(result4,type(result4))




