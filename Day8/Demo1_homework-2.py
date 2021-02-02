# @Author: Chris Paul
# @Time: 2021/01/28 22:54
# @File: Demo1_homework-2.py

# 定义一个软件测试工程师的类
class Tester:
    # 初始化函数：用于初始化参数，规定实例化函数的时候需要传进的参数
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        pass

    # 实例方法
    def earning(self):
        print(self.name + "赚钱")
        # self.singing()

    # 类方法，cls为必带参数，代表的是类实例本身，与self一样
    # 使用场景：当方法与其他类函数 类属性 没有关系时，就可以使用这个定义
    @classmethod
    def cooking(cls):
        print(cls)

    # 静态方法
    # 使用场景：当方法与其他类函数 类属性 没有关系时，就可以使用这个定义
    @staticmethod
    def singing():
        print("唱歌")

"""
1.实例方法self 类方法cls 静态方法（普通方法） 实例和类名都可以直接调用
2.不同点：
    a.静态方法 和 类方法 不可以调用类里面的属性值，如果要用到参数，需要自己传递参数
"""
if __name__ == '__main__':
    # 第一种实例化方法（推荐）
    tester = Tester()
    tester.__setattr__("name","CP3")
    tester.earning()
    # 第二种实例化方法
    # Tester.earning() # TypeError: earning() missing 1 required positional argument: 'self'
    # Tester.earning(Tester())
    # 第三种方法：直接就不需要实例化即可使用类里面的方法
    # 1.在类函数上面加上注解@classmethod
    # 2.直接调用即可，不用创建实例也可以调用，如下
    # Tester.cooking()
    # 第四种方法：静态方法@staticmethod,也是直接调用就可以了
    # Tester.singing()




