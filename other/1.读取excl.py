"""
@file: 1.读取excl
@author: Cooper.wy_zou1103@163.com
@date: 2021/03/15
@decs

"""
import xlrd,os,time

xlxs_path = r'C:\Users\dell\Desktop\LibVersion.xlsx'
work_book = xlrd.open_workbook(xlxs_path)


# 按索引、名称获取sheet表对象：
sheet_1 = work_book.sheet_by_index(0)
# 获取某一列
col_0_value = sheet_1.col_values(0)
# print(col_0_value)
col_1_value = sheet_1.col_values(1)
# print(col_1_value)


def file_path():
    list_dll = []
    for dll,file_version in zip(col_0_value,col_1_value):
        dll = dll.replace('.dll','')
        file = f'{dll}\{file_version}\{dll}.{file_version}.nupkg'
        # file_name = f'{dll}.{file_version}.nupkg'
        dll_path = os.path.join(r'C:\test',file)
        # print(dll_path)
        if os.path.exists(dll_path):
            list_dll.append(dll_path)
    return  list_dll

def get_file_rtime(filename):
    filemt = time.strftime('%Y/%m/%d',time.localtime(os.path.getmtime(filename)))
    # print(filemt)
    return filemt
# get_file_rtime("C:\\test\\abc\\Beisen.Amqp\\1.1.0.2\\Beisen.Amqp.1.1.0.2.nupkg")

# file_path()





if __name__ == '__main__':
    for path in file_path():
        res = get_file_rtime(path)
        with open('F:\\123.txt','a') as f:
            f.write(f'{path} {res}\n')


        print(path,res)










# rows = table1.get_rows()
# for row in rows:
#     print(row)


