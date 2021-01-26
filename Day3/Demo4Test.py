"""
1.询问用户性别和年龄
2.符合要求的可以加入足球队，询问5次
3.打印符合人数
count = 0
print("请输入年龄和性别")
for item in range(0,5):
    age = int(input("年龄："))
    sex = input("性别：")
    if 18 <= age < 25 and (sex == 'm' or sex == 'M'):
        print('符合要求')
        count += 1
    else:
        print("不符合标准")
print("满足条件的总人数：{0}".format(count))
"""
# 打印直角三角形
"""
i = 0
for i in range(10):
    for j in range(i):
        print("*",end="")
    print()
"""
# [['张三','李四','王五'],['婷婷'],['玉立']] 逐个输出里面所有元素
L = [['张三','李四','王五'],['婷婷'],['玉立']]
for items in L:
    for item in items:
        print(item)



