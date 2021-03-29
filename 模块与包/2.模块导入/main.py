"""
@file:   main
@author: linuxzhen520@163.com
@date:   2020/04/09
@desc:
"""


# 消除红线 => 右击 - mark directory as - sources root
# 注意 => 在一个项目，只设置一个目录为sources root
# 所有问题的产生一定是有原因的。

# 同一个模块导入两次
from pack01 import one
from pack01 import one
# 当同一个模块重复导入的时候，只执行(导入)一次

# 当导入同名的模块时 => 两个都被导入，谁生效呢？
from pack01 import three
from pack02 import three
# 当前生效的是pack02.three.show => 后导入的生效
three.show()


# 当导入同名的模块时，希望两个都生效
# => as 给导入的内容重命名
from pack01 import three as pack01_three
from pack02 import three as pack02_three
# 当前生效的是pack02.three.show => 后导入的生效
pack02_three.show()
pack01_three.show()


# 模块的名字比较长
from bs4 import BeautifulStoneSoup as Soup
print(Soup)
# 很多时候，大家都会有一些约定俗成的名字






