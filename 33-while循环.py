
def add_to_number(maxNumber):
    i = 0
    numbers = []

    while i <= maxNumber:
        numbers.append(i)
        print("正在添加%d",i)
        print("numbers are %s"%(numbers))
        i += 1

add_to_number(50)
