
def add(a,b):
    print ("%d+%d"%(a,b))
    return a+b

def subtract(a,b):
    print ("%d-%d"%(a,b))
    return a-b

def multiply(a,b):
    print("%d * %d"%(a,b))
    return a*b
def divide(a,b):
    print("%d / %d"%(a,b))
    return a/b


print("让我们做一些运算")

age = add(1,2)
height = subtract(5,4)
weight = multiply(10,10)
divide = divide(20,5)

print("所以最后 年龄是 %d，身高是 %d ， 体重是%d ， 除法的结果是%d"%(age,height,weight,divide))
