#接受一个文件名 读取文件

from sys import argv

script,txtname = argv

#要注意 open()是返回文件 并不是文件内容
txt = open(txtname)

print("这是%s文件的内容"%(txtname))
print(txt.read())

print("请再输入一次文件名")
file_name = input("> ")

txt_again = open(file_name)
print(txt_again.read())
