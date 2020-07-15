# coding=UTF-8
import os
 
#file_type = input("输入文件后缀名，直接回车修改所有文件\n请输入想要处理的文件类型(jpg/png/mp3/...)：")
#if file_type:
#    if not file_type.count("."):
#        file_type = "." + file_type
#    print("\n您想修改的文件后缀是",file_type,"\n")
#else:
#    print("\n您要修改的是所有文件。\n")
# 
#bits = input("序号位数(直接输入数字，默认为3)：")
#if bits.isdigit():
#    bits = int(bits)
#else:
#    bits = 3

file_type = ".jpg"
bits = 3

def check_type(file_type):
# 检查是否输入后缀的自定义函数
    if file_type:
        check = file.lower().endswith(file_type)
    else:
        check = True
    return check
 
print("========Start=======")
f_type = ""
files=os.listdir(os.curdir)
files.sort() #列表排序
for file in files:
    if check_type(file_type) and not file.endswith(".py") and not os.path.isdir(file):
        f_name,f_ext = os.path.splitext(file)
        # 把文件名分割成名称和后缀
        f_ext = f_ext.lower()
        # 把后缀全部转为小写
        if not f_type == f_ext:
        # 后缀变了之后，重新编码
            i = 0
            print("\n*** " + f_ext + "***\n")
        i += 1
        f_num = "{:0>3}".format(i)
        # 按照位数格式化数字
        f_new = "" + f_num + f_ext
        # 添加序号之后的新文件名
        f_type = f_ext
        os.rename(file,f_new)
        print(file,">",f_new)
print("========End=======")