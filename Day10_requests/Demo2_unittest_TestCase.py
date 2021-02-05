# FileName: Demo2_unittest
# Date：2021-02-05 09:17
# Author：CP3

import unittest
from Day10_requests.Math_Methods import Math_Method

"""
编写测试用例使用unittest.TestCase进行编写
就是说需要将测试用例类继承unittest.TestCase

测试加法的测试用例
1.两个正数相加
2.两个负数相加
3.两个0相加
4.均不输入（暂时不弄这个）
"""


class TestMathMethod_add(unittest.TestCase):
    # 1.两个正数相加
    def test_add_two_positive(self):
        result = Math_Method(1, 1).add()
        print("两个1相加，结果：{0}，预期结果：{1}".format(result, 2))

    # 2.两个负数相加
    def test_add_two_nagetive(self):
        result = Math_Method(-1, -2).add()
        print("-1和-2相加，结果：{0}，预期结果：{1}".format(result, -3))

    # 3.两个0相加
    def test_add_two_zero(self):
        result = Math_Method(0, 0).add()
        print("两个0相加，结果：{0}，预期结果：{1}".format(result, 0))


class TestMathMethod_multi(unittest.TestCase):
    def test_multi_two_positive(self):
        result = Math_Method(2, 2).multi()
        print("两个1相乘，结果：{0}，预期结果：{1}".format(result, 4))

    def test_multi_two_nagetive(self):
        result = Math_Method(-1, -2).multi()
        print("-1和-2相乘，结果：{0}，预期结果：{1}".format(result, 2))

    def test_multi_two_zero(self):
        result = Math_Method(0, 0).multi()
        print("两个0相乘，结果：{0}，预期结果：{1}".format(result, 0))

    if __name__ == '__main__':
        unittest.main()
