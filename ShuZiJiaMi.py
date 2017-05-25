#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#多维度密码加密以及查询
#三维
listA = ("2","3","4","5","6","7","8","9","0","1")
listB = ("4","5","6","7","8","9","0","1","2","3")
listC = ("6","7","8","9","0","1","2","3","4","5")
listD = ("8","9","0","1","2","3","4","5","6","7")
list0 = (listA,listB,listC,listD)

while True:
    question = input("请问你要干什么：1.加密。2.解密（查询原密）。输入其它=拜拜~：")

    if question == "1":
        userInputNumbers = input("请输入要加密的数字组合（4位）：")
        listN = [userInputNumbers[0], userInputNumbers[1], userInputNumbers[2], userInputNumbers[3]]
        print(listN)
        print(list0[2][int(listN[0])], list0[1][int(listN[1])], list0[3][int(listN[2])], list0[0][int(listN[3])])


    elif question == "2":
        userInputNumbers2 = input("请输入要解密的数字组合（4位）：")
        listM = [userInputNumbers2[0], userInputNumbers2[1], userInputNumbers2[2], userInputNumbers2[3]]
        print(list0[2].index(userInputNumbers2[0]), list0[1].index(userInputNumbers2[1]), list0[3].index(userInputNumbers2[2]),
              list0[0].index(userInputNumbers2[3]))
    else:
        print("拜拜~")
        break
