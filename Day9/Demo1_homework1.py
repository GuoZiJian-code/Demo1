# FileName: Demo1_homework1.py
# Date：2021-02-01 17:50
# Author：CP3
"""
按照以下要求定义一个游乐园门票类，并创建实例调用函数
完成儿童和大人的总票价统计（人数不定，由你输入的人数个数来决定）
1.平日票价100元
2.周末票价为平日票价120%
3.儿童半价
"""


class TicketCost:
    def __init__(self, age, day, price=100):
        self.price = price
        self.age = age
        self.day = day

    def TicketCost(self):  # 计算年龄段的票价
        if 15 <= self.age <= 18:
            return int(self.price)
        elif 0 <= self.age < 15:
            return int(self.price * 0.5)

    def TicketCostInWeekendOrWorkDay(self):  # 计算星期N的票价
        if self.day in range(1, 6):
            return int(self.TicketCost())
        elif self.day in range(6, 8):
            return int(self.TicketCost() * 1.2)
        else:
            return int(self.TicketCost())


if __name__ == '__main__':
    flag = "Y"
    ticketCostSum = 0
    while flag.lower() == "y":
        day = input("请问所需要购买星期几的票：")
        age = input("请问岁数：")
        if day.lower() == "q":
            print("当前需要总票费：{0}".format(ticketCostSum))
            print("退出")
            break
        elif age.lower() == "q":
            print("退出")
            break
        else:
            ticket = TicketCost(age=int(age), day=int(day))
            ticketCost = ticket.TicketCostInWeekendOrWorkDay()
            print("所需要购买的票价：{0}".format(ticketCost))
            ticketCostSum += ticketCost
            print("当前需要总票费：{0}".format(ticketCostSum))
