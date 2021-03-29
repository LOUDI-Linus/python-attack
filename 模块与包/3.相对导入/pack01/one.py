# . => pack01

from . import two
# .. => 3.相对导入 => 不是包
# from ..pack02 import three
# from .. import pack02
# ValueError: attempted relative import beyond top-level package


print("i am pack01.one")

def fun1():
    print("pack01.one.func1")

