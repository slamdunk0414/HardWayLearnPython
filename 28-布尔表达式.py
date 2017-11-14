def test(func,result):
    if func == result:
        print("对了")
    else:
        print("不对哦")

#1. True and True 真
test(True and True,True)
#2. False and True 假
test(False and True,False)
#3. 1==1 and 2==1 假
test(1==1 and 2==1,False)
#4. "test" == "test" 真
test("test" == "test",True)
#5. 1==1 or 2!=1 真
test(1==1 or 2!=1,True)
#6. True and 1 == 1 真
test(True and 1 == 1,True)
#7. False and 0 != 0 假
test(False and 0 != 0,False)
#8. True or 1==1 真
test(True or 1==1,True)
#9. "test" == "testing" 假
test("test" == "testing",False)
#10. 1 != 0 and 2== 1 假
test(1 != 0 and 2== 1,False)
#11. "test" != "testing" 真
test("test" != "testing",True)
#12. "test" == 1 假
test( "test" == 1,False)
#13. not(True and False) 真
test(not(True and False),True)
#14. not(1==1 and 0!=1) 假
test( not(1==1 and 0!=1),False)
#15. not(10 == 1 or 1000 == 1000) 假
test( not(10 == 1 or 1000 == 1000),False)
#16. not(1 != 10 or 3== 4) 假
test(not(1 != 10 or 3== 4),False)
#17. not("testing" == "testiong" and "Zed" == "Cool guy") 真
test(not("testing" == "testiong" and "Zed" == "Cool guy"),True)
#18. 1==1 and not("testind" == 1 or 1== 0) 真
test(1==1 and not("testind" == 1 or 1== 0),True)
#19. "chunky" == "bacon" and not (3 ==4 or 3==3) 假
test("chunky" == "bacon" and not (3 ==4 or 3==3),False)
#20. 3==3 and not("testing" == "testing" or "Python" =="Fun") 假
test(3==3 and not("testing" == "testing" or "Python" =="Fun"),False)
