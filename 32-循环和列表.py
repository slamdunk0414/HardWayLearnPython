

hairs = ["棕色","红色","蓝色"]
eyes = ["棕色","蓝色","绿色"]
weights = [1,2,3,4]

the_count = [1,2,3,4,5]
fruits = ["苹果","句子","梨","桃子"]

change = [1,"块",2,"八",3,"毛"]

for number in the_count:
    print("number is %d"%(number))

for fruit in fruits:
    print("水果分别是%s"%(fruit))

for i in change:
    print("I就是%r"%(i))

elements = []

for i in range(0,6):
    print ("把%d添加到列表里面"%(i))
    elements.append(i)

for i in elements:
    print("元素分别是%d"%(i))
