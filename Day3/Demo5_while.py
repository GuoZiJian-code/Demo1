# @Author: Chris Paul
# @Time: 2021/01/11 23:56
# @File: Demo5_while.py
# while
# 一个班级有一个花名册，存在列表里面
# 你从控制台输入一个名字，如果这个名字在花名册里面
# 就打印这个用户名正确，如果不存在，那就报错
usernames = ['张三','李四','王五','赵六','郭子健']
flag = 0
while flag == 0:
    userInput = input("请输入用户名：")
    if userInput.isdigit():
        flag = int(userInput)
        if flag == 0:
            print('退出')
            break
    else:
        if userInput in usernames:
            print("用户名正确")
        else:
            print("用户名错误")






