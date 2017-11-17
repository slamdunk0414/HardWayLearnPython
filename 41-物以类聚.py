'''
练习1

class TheThing(object):

    def __init__(self):
        self.number = 0;

    def add_me_up(self,more):
        self.number += more
        return self.number

a = TheThing();
b = TheThing();

print(a.add_me_up(20))
print(b.add_me_up(30))

print(a.number)
print(b.number)

class TheMultiplier(object):
    def __init__(self,base):
        self.base = base

    def do_it(self,more):
        return more * self.base

x = TheMultiplier(10)
print(x.do_it(b.number))

'''

#定义一个动物类 什么都不做
#定义一个狗类 狗有名字
#定义一个猫类 猫有名字
#定义一个人类 人有一个宠物

class Animal(object):
    def __init__(self,name):
        self.name = name
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Person(Animal):

    def __init__(self,name,dog):
        self.name = name
        self.dog = dog

        print("我的名字是%s"%(name))
        print("我有一只狗 狗的名字是%s"%(dog.name))

    pass


dog = Dog("wc")

p = Person("xx",dog)
