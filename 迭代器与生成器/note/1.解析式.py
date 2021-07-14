"""
@file:   1.解析式
@author: linuxzhen520@163.com
@date:   2020/05/06
@desc:
"""

"""
结果 => 列表
a => [1, 2, 3, 4]
b => [2, 4, 6, 8]

b = []
for i in a:
    if i%2==0:
        b.append(i*2)
    
b = [输出表达式 for 临时变量 in 数据序列 if 条件表达式]
b = [i*2 for i in a]
"""
a = [1, 2, 3, 4]


b = []
for i in a:
    if i % 2 == 0:
        b.append(i*2)
print(b)

c = [i*2 for i in a if i%2==0]
print(c)

a = {1,2,3,4}
#
b = [2,4,6,8]


# 找出30以内能被3整除的所有数字
# [输出表达式 for 临时变量 in 数据序列 if 条件表达式]
c = [i for i in range(30) if i%3==0]
print(c)

names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
 ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva', 'Elven']]


result = []
for item in names:
    for i in item:
        # 名字中包含两个e的所有名字， str => count
        if i.count('e') == 2:
            result.append(i)
print(result)

result = [i for item in names for i in item if i.count('e')==2]
print(result)

"""
列表推导式和if三元运算
100以内[0-99]能被2整除的所有的数据，如果能被4整除，转换成str，否则转换成float
"""
def get_data():pass

# 1
# result = [ str(item) if item%4==0 else float(item) for item in range(100) if item%2==0]
result = get_data()
print(result)


# 2
# result2=[]
# for item in range(100):
#     if item % 2 == 0:
#         if item % 4 == 0:
#             result2.append(str(item))
#         else:
#             result2.append(float(item))
result2 = get_data()
print(result2)

# 编程技巧
# 易懂： 2
# 简洁： 1
# 即易懂又简洁 => 封装函数/模块 => 1或2大段代码封装成一个函数 => 取一个有意义的名字，直接通过名字就能看出功能


"""
str(i) if i%4==0  else float(i)

if i % 4 == 0:
    str(i)
else:
    float(i)

流程控制 => if



[i for i in x]
[i for i in x if expres]
[i for i in x for ii in i if expres]
[x if 条件 else y for i in x for ii in i if expres]

"""

q1 =  ['a','ab','abc','abcd','abcde']
result = [ i.upper() for i in q1 if len(i) >=3 ]
result = [ i.upper() for i in q1 if i.__len__() >=3 ]
print(result)


# [(x,y),(x,y),(x,y)]
# [(0,1),(0,3),(0,5),(2,1),(2,3),(2,5),(4,1),(4,3),(4,5)]
for x in range(6):
    if x %2 == 0:
        for y in range(6):
            if y%2 ==1:
                print(x,y)
result = [(x,y) for x in range(6) if x%2==0 for y in range(6) if y%2==1]
print(result)
result = [(x,y) for x in range(6) if x%2==0 for y in range(6) if y%2!=0]
print(result)

# for x in range(0,6,2):
#     for y in range(1,6,2):
#        print(x,y)
# result = [(x,y) for x in range(0,6,2) for y in range(1,6,2)]
# print(result)



# 字典推导式
"""
结果 => 字典  {key:value, key:value}
[i for i in x if expres]

{key:value for item in obj}
"""

dic = {'a':1, 'b':2, 'c':3, 'ab':4}
# {'b':2, 'c':3}
result = { key:dic[key] for key in dic if 'a' not in key}
print(result)

q3 = {'a': 10, 'b':34}
result = {value:key for key,value in q3.items()}
print(result)

q4 = {'B':3, 'a':1, 'b':6, 'c':3, 'A':4}
# key不区分大小写了，统一用小写表示
# result = {'a': 5, 'b': 9, 'c':3}
result = {}
for key,value in q4.items():
    result[key.lower()] = q4.get(key.lower(),0)+q4.get(key.upper(),0)
    # result[key.lower()] = q4[key.lower()] +q4[key.upper()]
print(result)

result = {key.lower():q4.get(key.lower(),0)+q4.get(key.upper(),0) for key in q4}
print(result)


q4 = {'B': 3, 'a': 1, 'b': 6, 'c': 3, 'A': 4}
result = {key.lower(): q4[key.lower()]+q4[key.upper()] if key.lower() in q4 and key.upper() in q4 else q4[key] for key in q4}
print(result)
