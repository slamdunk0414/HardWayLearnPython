
stuff = {"name":"zp","age":10,"weight":20}

print("姓名是",stuff["name"])

print("年龄是",stuff["age"])


#字典添加元素

stuff[1] = "hehe"

print(stuff)

#删除元素
del stuff[1]
print(stuff)

cities = {'BJ':'北京','SH':'上海','HB':'河北'}
cities['CQ'] = '重庆'
cities['HN'] = '海南'

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "not found"

cities['_find'] = find_city

while True:
    print ("请输入一个城市简写 如果不想输入 直接按回车")
    state = input(">")

    if not state:
        print("退出程序")
        break;

    city_found = cities['_find'](cities,state)
    print (city_found)



#第三版的练习

class Song(object):
    def __init__(self,songs):
        self.songs = songs;

    def sing(self):
        for song in self.songs:
            print(song)

happy = Song(["111","222","333"])
happy.sing()
