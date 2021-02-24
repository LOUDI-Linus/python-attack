"""
@file: 2.str与bytes转换
@author: Cooper.wy_zou1103@163.com
@date: 2021/02/22
@decs
python3中的字符串类型
    bytes
       转换 ----bytes->str: decode(utf8)
    str
       反之     encode
"""
# str->bytes
mystr = "你好"
mystr_bytes = mystr.encode()
print(mystr_bytes)

# bytes->str
mystr_str = mystr_bytes.decode()
print(mystr_str)

# bytes => 只有asscii表中数据才能b
mystr_bytes2 = b"123456"
print(mystr_bytes2.decode(),type(mystr_bytes2))