from sys import argv
from os.path import exists

script , from_file, to_file = argv

print("正在从%s文件拷贝到%s文件"%(from_file,to_file))

fromFile = open(from_file)
fromContent = fromFile.read()

print("复制的文件有%d个字节"%(len(fromContent)))

print("目标文件存在吗？ %r"%(exists(to_file)))

print("准备好了 开始复制")

#找到目标文件 open操作如果没有会创建
toFile = open(to_file,'w')
#现将目标文件清空
toFile.truncate()

#写入拷贝文件
toFile.write(fromContent)

#最后将两个文件都关闭
fromFile.close()
toFile.close()
