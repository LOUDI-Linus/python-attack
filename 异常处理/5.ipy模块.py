"""
@file:   5.ipy模块
@author: linuxzhen520@163.com
@date:   2020/04/10
@desc:
"""

from IPy import IP

ip = input("请输入一个ip地址或网段:")
# 转换ip实例:注意，要输入一个合法的网段
# 19.168.9.0/24  => C段

ips = IP(ip)
print(ips)
if len(ips) > 1:
    print("这是一个网段")
    print("网段", ips.net())
    print("子网掩码", ips.netmask())
    for item in ips:
        print(item)
        cmd = f"ping {item} -n 1 -w 1"
        import os
        # os.system执行系统命令
        ret = os.system(cmd)
        print('ret',ret)
        # 如果ret是0表示item是通的，存活
        # 如果ret是1表示不通，不存活
else:
    print("这是一个ip地址")

"""文件内容
a.txt => 活
192.168.0.1

b.txt => 不存活
192.168.0.2
"""


