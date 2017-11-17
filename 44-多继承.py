class Base(object):
    def test(self):
        print("base")

class A(Base):
    pass
#    def test(self):
#        print("a")

class B(Base):
    def test(self):
        print("b")

class C(A,B):

#如果想指定父类 可以写上类名。方法
    def test(self):
        B.test(self)

c = C()
c.test()

#使用 类名.__mro__ 查看类的继承关系
