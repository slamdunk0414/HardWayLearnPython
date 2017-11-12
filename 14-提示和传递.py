from sys import argv

scrpit , user_name = argv

prompt = ' > '

print("你好%s 我是%s脚本"%(user_name,scrpit))
print("我要问你一些问题")

print("你喜欢我吗 %s"%(user_name))

like = input(prompt)

print("你在哪里住呢 %s"%(user_name))

where = input(prompt)

print("你喜欢哪种电脑 %s"%(user_name))

com = input(prompt)

print("""

所以 你对我%s

你住在%s

你喜欢%s电脑

"""%(like,where,com))
