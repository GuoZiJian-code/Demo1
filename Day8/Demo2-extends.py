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


class RobotTwo(RobotOne):  # 二代机器人
    def walking_on_ground(self):  # 重写
        print("{0}可平稳的在平地行走".format(self.name))

    def walking_avoid_block(self):  # 拓展
        print("{0}可避开障碍物".format(self.name))


if __name__ == '__main__':
    robotTwo = RobotTwo("2018", "机器人一号")
    robotTwo.showInformation()
    robotTwo.walking_on_ground()
    robotTwo.walking_avoid_block()
