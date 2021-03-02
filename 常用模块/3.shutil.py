"""
@file: 3.shutil
@author: Cooper.wy_zou1103@163.com
@date: 2021/03/02
@decs

"""
""""
shutil.copyfileobj(open(old,'r'),open(new,'w')) 将文件拷贝到另一个文件
shutil.copyfile('x','y')   拷贝文件内容
      .copymode-----------拷贝权限
      .copystat  仅拷贝状态信息
      .copy   拷贝文件和权限
      .copy2  拷贝文件和状态信息


"""
# 小练习
# !/usr/bin/python3 python3
import os,shutil

path_dir="/tmp/test"
file_dir = ["os","23","shutil"]
list1 = ["liu.txt","guan.txt","zhang"]

for item in file_dir:
    os.mkdir(os.path.join(path_dir,item))

os.chdir("/tmp/test/os")
for item in list1:
    os.mknod(os.path.join((os.getcwd()),item))

shutil.move("/tmp/test/os/zhang","/tmp/test/23/zouweicheng")

shutil.copytree("/tmp/test/os","/tmp/test/shutil/today")
# shutil.rmtree()

print("#######################bingo")
