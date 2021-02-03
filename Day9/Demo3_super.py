# FileName: Demo3
# Date：2021-02-02 17:33
# Author：CP3

class calcuMethod:
    def __init__(self, a, b, step = 0):
        self.a = a
        self.b = b
        self.step = step

    def add(self):
        print("我是父类的加法", self.a + self.b)

    def sub(self):
        print(self.a - self.b)


class calcuMethod_1(calcuMethod):
    def add(self):
        super(calcuMethod_1, self).add()
        print("我是子类的加法", self.a + self.b + self.step)


if __name__ == '__main__':
    calcuMethod_1(10, 2, 20).add()
