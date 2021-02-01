# @Author: Chris Paul
# @Time: 2021/01/31 22:12
# @File: Demo2_homework.py

# 编写一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性，在User类中定义一个名为describe_user的方法，打印用户信息摘要，再定一个greet_user()的方法
# 向用户发出个性化问候，创建多个表示不同用户的实力，并对上面每个实例都调用上述两种方法
class User:
    def __init__(self, first_name, last_name,*label):
        self.first_name = first_name
        self.last_name = last_name
        self.label = label

    def describe_user(self):
        print("用户初始名：{0}，用户最新名：{1}，个人标签为:{2}".format(self.first_name,self.last_name))
        self.greet_user()

    def greet_user(self):
        print("您好，{0}".format(self.last_name))

if __name__ == '__main__':
      user = User("子健","郭子健",("哈哈哈"))
      user.describe_user()