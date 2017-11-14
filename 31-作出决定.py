print("你来到一个黑暗的房间 这里有两扇门 你要走过1还是2？")

door = input(">")

if door == "1":
    print("你到了第一扇门后面 这里有一个吃蛋糕的胸 你要？")
    print("1 拿走蛋糕")
    print("2 吓走熊")

    bear = input(">")

    if bear == "1":
        print("熊吃掉了你的头")
    elif bear == "2":
        print("熊吃掉了你的腿")
    else:
        print("熊跑掉了")

elif door == "2":
    print("这里有一些吃的 你要？")
    print("1蓝莓")
    print("2草莓")
    print("3香蕉")

    eat = input(">")

    if eat == "1":
        print("有毒 拜拜")

    elif eat == "2":
        print("还是有毒")
    else:
        print("好了 你过关了")

else:
     print("掉进了机关 再见")
