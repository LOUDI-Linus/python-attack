"""
@file: 解析式
@author: Cooper.wy_zou1103@163.com
@date: 2021/07/12
@decs

"""
a = [i for i in range(1,10)]
b=[i for i in a if i%2==0]
print(b)

names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
 ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva', 'Elven']]

result = []
for item in names:
    for i in item:
        if i.count("e")==2:
            result.append(i)
print(result)

# 100以内[0-49]能被2整除的所有的数据，如果能被4整除，转换成str，否则转换成float
num = list(range(1,50))

result2 = [str(i) if i%4==0 else float(i) for i in range(1,50) if i%2==0]
print(result2)

# 封装函数
def get_data():
    """返回相应的数据"""
    result10=[]
    for i in range(1,50):
        if i%2==0:
            if i%4==0:
                result10.append(str(i))
            else:
                result10.append(float(i))
    return result10

x=get_data()
print(x)
