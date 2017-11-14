人= 30
汽车 = 40
公交车 = 15

if 汽车 > 人:
    print("我们可以开车")
elif 汽车 < 人:
    print("我们不能开车")
else:
    print("随便吧")

print("----------")

if 公交车>汽车:
    print("公交车太多了 来坐🚌")
elif 汽车>公交车:
    print("🚗太多 来坐坐🚗吧")
else :
    print("随便吧")

print("----------")

if 人>公交车:
    print("可以坐🚌")
else:
    print("在家不出门")
