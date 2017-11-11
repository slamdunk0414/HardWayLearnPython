from sys import argv

script,first,second,third = argv

print("脚本运行了",script)

print("第一个参数是",first)

print("第二个参数是",second)

print("第三个参数是",third)

#运行此py需要执行 python3 py名 +三个参数

#如果参数不够 会报错ValueError: not enough values to unpack (expected 4, got 3)
