# @Author: Chris Paul
# @Time: 2021/01/19 23:21
# @File: Demo4_Homework.py
def checkStrLen(_str):
    if len(_str) > 2:
        return _str[0:2]


print(checkStrLen(input("输入字符:")))
