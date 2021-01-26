# @Author: Chris Paul
# @Time: 2021/01/18 20:38
# @File: Demo1_Function.py.py
# Python的内置函数
# print input len type str int float double list range
# pop insert append split strip replace remove clear
"""
函数名应注意的点：
函数名命名的规范：小写字母 不能以数字开头 不同的字母之间用下划线隔开
函数的特点：
1.可重复使用，可复用性
"""


# 定义函数：
# 函数的语法:def 关键字
# 1.不指定参数
# def 函数名():
#   函数体:希望这个函数所实现的功能
def shoutSlogan_NoArgument():
    print("月薪上万！")


# 2.指定参数
# def 函数名(参数1,参数2,参数3): 可传多个参数,调用时接参
#   函数体:希望这个函数所实现的功能
def shoutSlogan_WithArgument(name):
    print("{0}，他月薪上万！".format(name))


# 3.指定默认参数
# def 函数名(参数1=默认值):
#   函数体:希望这个函数所实现的功能
def shoutSlogan_WithDefaultArgument(name="郭子健"):
    print("{0},努力月薪上万！".format(name))


# 调用函数
shoutSlogan_NoArgument()  # 月薪上网！
shoutSlogan_WithArgument('张三')  # 张三，他月薪上万！
shoutSlogan_WithDefaultArgument()  # 郭子健,努力月薪上万！


# 请把1-100的连续整数相加，写成一个函数
def _caculateSum():
    sum = 0
    for i in range(1, 101):
        sum += i
    print("1-100总和：{0}".format(sum))


# _caculateSum()

# 利用range函数请求出任意两个整数之间的连续整数相加，写成一个函数
def _caculateSum(start, end, step=1):
    sum = 0
    for i in range(start, end, step):
        sum += i
    print("1-100总和：{0}".format(sum))


_caculateSum(1, 11000, 1)
"""
当要把一个功能变成一个函数，所需要做的步骤是（操作的步骤）
1.先用代码实现功能，还可以选取一组数据去验证代码是否正确
2.变成函数，加def
3.想办法提高代码的复用性
"""
