"""
@file: 生成器
@author: Cooper.wy_zou1103@163.com
@date: 2021/07/13
@decs

"""
# 生成器是一种特殊的迭代器

def func1():
    x = 8
    # 生成器函数 => 调用该函数会创建一个生成器,yield直接返回表达式的结果,同时保存当前的状态
    yield x
    y = 2
    yield y
    z = 3
    yield z

f =func1()
print(next(f))
print(next(f))
print(type(func1), f)

def func2():
    a=1
    b=2
    while True:
        yield b
        a, b = a, a+b

f = func2()

# 取前10项，并且保存
result = [next(f) for i in range(10)]
print(result)

for i in f:
    # for隐藏调用next
    print(i)
    if i >10:
        break

def counter(start_at=0):
    count = start_at
    while True:
        val = yield count
        if val is not None:
            count = val
        else:
            count += 1

count = counter(5)
# 等价于print(count.send(None))
print(next(count))

print(count.send(1))
print(next(count))
print(next(count))

print(count.send(100))
# 关闭
count.close()
def func():
   print('Python')
   yield '第一个yield'
   print('生成器')
   yield '第二个yield'
   a = 1
   b = 2
   c = a + b
   print(c)
   yield '第三个yield'

ret = func()
print(next(ret))
# print(next(ret))
# print(next(ret))

# def read_file(fpath):
#     BLOCK_SIZE = 3
#     with open(fpath,'rb') as f:
#         return f.read(BLOCK_SIZE)
#
# print(read_file("xxx"))

def read_file(fpath):
    BLOCK_SIZE = 3
    with open(fpath, 'rb') as f:
        block = f.read(BLOCK_SIZE)
        while True:
            if block:
                yield block
            else:
                return


a = read_file("xxx")
print(next(a))
