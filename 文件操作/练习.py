"""
@file: 练习
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/24
@decs

"""
import random

def create_file(file_name:str) -> None:
    """创建文件"""
    with open(f'{file_name}',mode='a+',encoding='utf8') as f:
        for i in range(100):
            line = f"172.25.254.{random.randint(1,25)}\n"
            f.write(line)

def counter_top_10(file_name:str) -> list:
    result = dict()
    with open(file_name,mode='r',encoding='utf8') as f:
        for ip in f:
            ip = ip.strip()
            if ip in result:
                result[ip] += 1
            else:
                result[ip] = 1
    # 排序
    return sorted(result.items(),key=lambda x:(x[1],x[0]),reverse=True )[:10]
file_name='ips.txt'
create_file(file_name)
result = counter_top_10(file_name)
print(result)



