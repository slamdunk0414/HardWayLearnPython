people = 20
cats = 30
dogs = 15

if people < cats:
    print("🐱太多了 世界将被破坏")

if people > cats:
    print("没有太多的🐱 世界被拯救了")

if people < dogs:
    print("🐶太多了")

if people > dogs:
    print("🐶太少了")

dogs += 5

if people >= dogs:
    print("人类数量大于等于🐶的数量")

if people <= dogs:
    print("人类小于🐶的数量")

if people == dogs:
    print("人🐶一样")
