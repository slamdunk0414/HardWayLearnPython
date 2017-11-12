#close 关闭
#read 读取
#readline 读取一行
#write("") 写入
#truncate 清空


from sys import argv

script , txtname = argv

print("我要将%s文件内容清空了"%(txtname))

print("如果不想清空 请按ctrl+v")

print("确定吗")

input("?")

print("正在打开。。。")

target = open(txtname,'w')
target.truncate()

print("现在要写入一些数据")

txt1 = input("写入第一行")
txt1 += ("\n")
txt1 += input("写入第二行")
txt1 += ("\n")
txt1 += input("写入第三行")

target.write(txt1)

print("拜拜")

target.close()
