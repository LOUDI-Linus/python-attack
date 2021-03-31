"""
@file:   5.ipy模块
@author: linuxzhen520@163.com
@date:   2020/04/10
@desc:
"""

# from IPy import IP
#
# ip = input("请输入一个ip地址或网段:")
# # 转换ip实例:注意，要输入一个合法的网段
# # 19.168.9.0/24  => C段
#
# ips = IP(ip)
# print(ips)
# if len(ips) > 1:
#     print("这是一个网段")
#     print("网段", ips.net())
#     print("子网掩码", ips.netmask())
#     for item in ips:
#         print(item)
#         cmd = f"ping {item} -n 1 -w 1"
#         import os
#         # os.system执行系统命令
#         ret = os.system(cmd)
#         print('ret',ret)
#         # 如果ret是0表示item是通的，存活
#         # 如果ret是1表示不通，不存活
# else:
#     print("这是一个ip地址")

# user_ip = '10.129.104.73'
# ip_mask = '255.255.254.0'

user_ip = input("请输入ip: ")

ip_mask = input("请输入子网掩码: ")

def ips_alive(user_ip,ip_mask):
    """
    网段存活IP检测
    """
    from IPy import IP
    import os

    ip_list=[]
    ips=(IP(f'{user_ip}').make_net(f'{ip_mask}'))
    print(ips)
    for item in ips:
        cmd = f"ping {item} -n 1 -w 1  "
        ret = os.system(cmd)
        print(ret)
    #     item=str(item)
    #     ip_list.append(item)
    # return ip_list

print(ips_alive(user_ip=user_ip,ip_mask=ip_mask))


"""文件内容
a.txt => 活
192.168.0.1

b.txt => 不存活
192.168.0.2
"""


