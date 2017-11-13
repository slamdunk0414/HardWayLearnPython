#引入包
from sys import argv

#获取传递的参数
script, input_file = argv

#定义一个打印全部的方法
def print_all(f):
    print(f.read())

#定义一个回到开始的方法
def rewind(f):
    f.seek(0)

#打印一行
def print_a_line(line_count, f):
    print(line_count)
    print(f.readline())
#打开文件
current_file = open(input_file)
print ("First let's print the whole file:\n")

#打印全部
print_all(current_file)

#回到初始位置
print ("Now let's rewind, kind of like a tape.")
rewind(current_file)
print ("Let's print three lines:")

#一行一行打印
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
