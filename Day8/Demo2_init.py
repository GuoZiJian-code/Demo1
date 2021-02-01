# @Author: Chris Paul
# @Time: 2021/01/31 17:48
# @File: Demo2_init.py

class Teacher:
    def __init__(self, name, sex, age, salary):
        self.name = name
        self.sex = sex
        self.age = age
        self.salary = salary

    def showInformation(self):
        # print("该教师名字为" + self.name + ",性别为" + self.sex + ",年龄为" + self.age)
        print("该教师名字为{0},性别为{1},年龄为{2}".format(self.name, self.sex, self.age))

    def showSalary(self):
        print("本月工资" + self.salary)

    @staticmethod
    def showAbility(*abilitys):
        ability_str = ""
        for item in abilitys:
            ability_str = item if ability_str == '' else ability_str+'、' + item
        print("才艺为{0}".format(ability_str))

    @classmethod
    def duty(cls):
        print("职责就是教学，不需要依赖任何参数")


if __name__ in '__main__':
    teacher = Teacher('郭子健', '男', '22', '11000')
    Teacher.duty()
    teacher.showInformation()
    teacher.showAbility("敲代码","会做饭","方便面")
    teacher.showSalary()
