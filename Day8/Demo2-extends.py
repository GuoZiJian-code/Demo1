# FileName: Demo2-extends.py
# Date：2021-02-01 12:03
# Author：CP3


class RobotOne:  # 一代机器人
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def showInformation(self):
        print("该{0}机器人为{1}年生产，是中国生产的机器人".format(self.name, self.year))

    def walking_on_ground(self):
        print("{0}可走在平地，但遇到障碍物就摔倒".format(self.name))


class RobotTwo:  # 二代机器人
    def __init__(self, name):
        self.name = name

    def walking_on_ground(self):  # 重写
        print("{0}可平稳的在平地行走".format(self.name))

    def walking_avoid_block(self):  # 拓展
        self.showInformation()
        print("{0}可避开障碍物".format(self.name))


# 多继承注意点：需要继承的几个类不能有互相继承关系，不然会报错
# 具有两个父类的属性和方法，如果两个父类具有同名的方法和属性的时候，就近原则，现在第一个继承类里面找，第一个继承类没有就去第二个继承类里面找
class RobotThree(RobotTwo, RobotOne):
    def jump(self):
        print(self.name + "可以单膝跳跃")


if __name__ == '__main__':
    robotThree = RobotThree("第三代机器人")
    robotThree.jump()
