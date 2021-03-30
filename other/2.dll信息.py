"""
@file: 2.dll信息
@author: Cooper.wy_zou1103@163.com
@date: 2021/03/15
@decs

"""

import os

root_path=r'C:\test\abc'
v1_dires = os.listdir(root_path)

for dire in v1_dires:
    v2_dires = os.path.join(root_path,dire)
    version_dires=(os.listdir(v2_dires))

    for version_dire in version_dires:
        print(os.listdir(os.path.join(v2_dires,version_dire)))







