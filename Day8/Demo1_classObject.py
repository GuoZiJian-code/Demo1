# @Author: Chris Paul
# @Time: 2021/01/28 22:21
# @File: Demo1_classObject.py.py
"""
类：类名的规范，大写开头，驼峰
class 类名：
    类属性
    def 类函数名(self):
        类函数内容

类的实例化：
类的实例名 = 类名()
类的调用
类的实例名.类属性/类函数

"""


class GirlFriend:
    weight = 85
    height = 160
    job = "会计"

    def print_self(self):
        print(self)

    def cooking(self):
        print("会做饭")

    def earning(self):
        print("会赚钱")


if __name__ in '__main__':
    girlFriend = GirlFriend()
    print("身高：{0}\n体重：{1}\n职业：{2}".format(girlFriend.height,girlFriend.weight,girlFriend.job))
    girlFriend.cooking()
    girlFriend.earning()
    girlFriend.print_self()
