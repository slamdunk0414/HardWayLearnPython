#用def定义一个函数

def print_two(*args):
    arg1,arg2 = args
    print(arg1)
    print(arg2)

def print_two_again(arg1,arg2):
    print(arg1)
    print(arg2)

def print_one(arg1):
    print(arg1)

def print_none():
    print("随便打印")

print_two("123","456")
print_two_again("hehe","world")
print_one("111")
print_none()
