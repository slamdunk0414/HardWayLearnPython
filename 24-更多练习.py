

print ("试着打印一些东西")

poem = """

常记溪亭日暮，沉醉不知归路，
兴尽晚回舟，误入藕花深处。
争渡，争渡，惊起一滩鸥鹭。

"""

print("----------")

print(poem)

print("----------")

six = 4 + 3 - 5 + 4
print ("这就是六：%d"%(six))

def hero(started):
    power = started * 50
    iq = power / 20
    agile = power / 10
    return power,iq,agile

start = 2
power,iq,agile = hero(start)

print("初始等级是%d"%(start))
print("英雄力量是%d"%(power))
print("智利是%d"%(iq))
print("敏捷是%d"%(agile))
