def break_words(stuff,word):
    print("将字符串%s 用%s分割"%(stuff,word))

    words = stuff.split(word)
    return words

words = break_words("1122333322113322211637276336622","22")

print(words)

def sort_words(words):
    """ 对words进行排序 """
    return sorted(words)

def print_first_word(words):
    """ 打印words中的第一个单词"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """ 打印words中的最后一个单词 """
    word = words.pop(-1)
    print(word)

def print_first_and_last(sentence):
    words = break_words(sentence," ")

    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = break_words(sentence,' ')
    words = sorted(words)

    print_first_word(words)
    print_last_word(words)

print_first_and_last_sorted("hehe haha nihao w shi ni da ye")
print_first_and_last("hehe haha nihao w shi ni da ye")
