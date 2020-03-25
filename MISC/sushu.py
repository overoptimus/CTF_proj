# coding=utf-8
import math
number = int(raw_input("Enter a number: "))
list = []


def getChildren(num):
    print '*' * 30
    isZhishu = True
    for i in range(2, int(math.sqrt(1 + num)) + 1):  # 多加个1
        if num % i == 0 and i != num:
            list.append(i)
            isZhishu = False
            getChildren(num / i)
            break
    if isZhishu:
        list.append(num)


getChildren(number)
print list
