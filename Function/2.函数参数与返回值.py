"""
@file: 2.函数参数
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/05
@decs

"""
"""            传递参数              """

# 位置参数---实参顺序相同于位置参数
def messgae(name, sex):
    """显示个人信息"""
    print(name + " and " + sex)

messgae("zwc", 'male')

# # 关键字传参
messgae(sex="male", name="zwc")


# 默认值--未传参，则用默认值------使用默认值时，形参列表先列出无默认值，在列出有默认的
def messgae(name, sex="none"):
    print(name + " and " + sex)

messgae('zwc', 'male')


"""             函数返回值           """
def get_message(first_name,last_name,middle_name=''):
    if middle_name:
        name = first_name + middle_name + last_name
    else:
        name=first_name+" "+last_name
    return name



while True:
    f_name=str(input("firstname: "))
    if f_name == "exit":
        break
    m_name=str(input("middle_name: "))
    if m_name == "exit":
        break
    l_name=str(input("lastname: "))
    if l_name == "exit":
        break

    print(get_message(f_name,l_name,m_name))

"""         传递列表      """

def guest_users(names):
    for name in usernmaes:
        print("hello "+name)


usernmaes=['zwc','cmz','zs','ls']
guest_users(usernmaes)


"""         函数中修改列表         
非必要不要向函数传递列表副本，虽可保留原内容，会花费多余时间，和内存，尤其是大型列表
"""
un_print_usernmaes=['zwc','cmz','zs','ls']
b=un_print_usernmaes[:]
print_usernames=[]

def print_names(names):
    while b:
        name=b.pop()
        print_usernames.append(name)

print_names(b)

def show_usernames(show_names):
    for name in print_usernames:
        print(name)

show_usernames(print_usernames)

print(print_usernames)
print(un_print_usernmaes)
print(b)

"""         传递任意数量实参
       python先匹配位置实参，然后是关键字，在最后是将剩余的传给最后一个形参
       **xx 形参为任意关键字实参，接受任意数量的键值对
       """
def make_pizzza(size,*toppings):
    """"    *xx代表创建了空元组， """
    print(size,toppings)

make_pizzza(16,"121212")