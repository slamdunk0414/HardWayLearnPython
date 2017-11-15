ten_things = "苹果 橙子 电话 糖 哈哈"

print("等等 现在还没到十件事 添加一下")

more_things = ["xx","yy","zz","oo","00","小黑","小白","小黄"]

stuff = ten_things.split(' ')

while len(stuff) != 10:
    string = more_things.pop()
    print("正在往列表里添加",string)
    stuff.append(string)
    print("现在列表里有%d个元素"%(len(stuff)))
