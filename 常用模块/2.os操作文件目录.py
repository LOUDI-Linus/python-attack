"""
@file: 2.os操作文件目录
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/26
@decs

"""

""" linux下操作  
os.getcwd()=pwd
os.listdir() ls -a
os.chdir("转换目录")

路径操作
os.path.split("/opt/1234.txt")   路径分割
os.path.join('/opt', '1234.txt') 拼接路径
os.path.splitext("/opt/1234.txt")   分离拓展名，以.XXX 为分割
os.path.dirname(os.getcwd(xx)) 获取上级路径
os.path.basename("/opt/1234.txt")  获取文件名，返回1234.txt
os.path.getsize(filename)   获取文件大小

目录文件操作
os.mkdir() 创建单目录
   makedirs（）多级目录  ------- mkdir -p
   os.mknod   创建空文件
   os.remove()  删除文件
      rmdir 只能删除空目录
      rename(old,new)
      stat()  ------------linux stat
      chmod("xxx",600)         修改文件权限
      
      


小练习
import os
os.mkdir("/opt/imgs")

path_file='/opt/imgs'

for item in range(1,10):
    os.mknod(f"/opt/imgs/{item}.png")

for item in os.listdir(path_file):
    os.rename(os.path.join(path_file,item),os.path.join(path_file,'sanchuang-'+item))

for item in os.listdir(path_file):
    filename,ext = os.path.splitext(item)
    if ext == ".png":
        os.rename(os.path.join(path_file,item),os.path.join(path_file,filename+".jpg"))


"""

