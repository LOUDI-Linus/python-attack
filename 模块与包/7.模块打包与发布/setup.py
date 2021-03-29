"""
@file:   setup.py
@author: linuxzhen520@163.com
@date:   2020/04/09
@desc:

pip 安装
源码安装
进入对应目录-
            python setup.py install


terminal-----运行
python setup.py check   检查配置是否正确
running check ------OK


生成安装包
python setup.py sdist
会生成一些文件
dist(xxxxxx)

找到目录解压文件，然后pip install 安装即可
"""

from setuptools import setup, find_packages

# 打包配置
setup(
    # key=value
    # pip list 显示的名字
    name = "Super-Game",
    # 官网
    url = "http://www.beisen.com",
    # 版本信息 => 按照格式来写，不能随便写
    version = "0.3.0",
    # 包都需要加__init__.py文件
    # 打包哪些东西? => find_pacakges会自动打包指定的目录下所有的数据
    packages = find_packages("src"),
    # src目录为空，直接从pake01导入
    package_dir = {"":"src"},
    # 打包模块, 如果有上面的打包src目录,py_modules可以不要
    # py_modules = ["model"],
    # 依赖信息 => 安装的时候,会自动帮我们安装好这个依赖
    install_requires = ["xlrd==1.2.0"],
    # 作者
    author = "zou",
    author_email = "wy_zou1103@163.com",
    description = "this is a game"
)