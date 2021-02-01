# @Author: Chris Paul
# @Time: 2021/01/28 22:54
# @File: Demo1_homework-1.py

# 定义一个软件测试工程师的类
class Tester:
    name = '郭子健'
    age = 22
    salary = 6000

    @classmethod
    def cooking(cls):
        print(cls)

    def earning(self):
        print("赚钱")

if __name__ == '__main__':
    # 第一种实例化方法（推荐）
    tester = Tester()
    tester.earning()
    # 第二种实例化方法
    # Tester.earning() # TypeError: earning() missing 1 required positional argument: 'self'
    Tester.earning(Tester())
    # 第三种方法：直接就不需要实例化即可使用类里面的方法
    # 1.在类函数上面加上注解@classmethod
    # 2.直接调用即可，如下
    Tester.cooking()


