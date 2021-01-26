# @Author: Chris Paul
# @Time: 2021/01/13 23:36
# @File: Homework.py
"""
有一个4位数的密码，对其进行加密
1.每位数乘以5,然后用取余
2.第一位和最后一位进行调换，第二位和第三位进行调换
3.输出

num = 9563
numStr = "%d" %num
numList = []
for item in numStr:
    item = int(item)
    item *= 5
    item %= 9
    numList.append(item)
print(numList) # 0736
i = 0
j = len(numList) - 1
temp = 0
for a in range(len(numList)):
    temp = numList[i]
    numList[j] =numList[i]
    numList[i] = temp
    i += 1
    j -= 1
print(numList)
"""

userInfos = {
    "ZhangSan":"123456",
    "Lisi":"654321",
    "wangwu":"145236"
}

errorCount_username = 3
while errorCount_username > 0:
    username = input("请输入用户名：")
    if username.upper() == 'Q':
        print('退出')
        break
    if username in userInfos.keys():
        errorCount_username = 3
        errorCount_password = 3
        while errorCount_password > 0:
            password = input("请输入密码：")
            if password == userInfos[username]:
                errorCount_password = 3
                print("密码正确")
                break
            else:
                errorCount_password -= 1
                print("密码错误，还剩{0}次机会".format(errorCount_password))
                if errorCount_password == 0:
                    break
    else:
        errorCount_username -= 1
        print("用户名错误，还剩{0}次机会".format(errorCount_username))
        if errorCount_username == 0:
            break
























