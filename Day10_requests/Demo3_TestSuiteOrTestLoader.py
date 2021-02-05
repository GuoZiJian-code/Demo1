# FileName: Demo3_TestSuiteOrTestLoader
# Date：2021-02-05 09:39
# Author：CP3


import unittest
from Day10_requests.Demo2_unittest_TestCase import TestMathMethod_add


# 执行用例
class runMath_MethodTestCase:
    if __name__ == '__main__':
        """
        第一种方法：使用TestSuite
            # 创建一个用例集合，TestSuite
            suite = unittest.TestSuite()
            # 往这个用例集合里面测试用例
            suite.addTest(TestMathMethod_add("test_add_two_positive"))
            suite.addTest(TestMathMethod_add("test_add_two_zero"))
            # 实例化一个执行实例TextTestRunner
            runner = unittest.TextTestRunner()
            # 执行用例集合，将集合放入执行实例的执行方法中
            runner.run(suite)
        """

        """
        第二种方法：使用TestLoader
        """
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        # 具体到某个功能的用例点
        # suite.addTest(loader.loadTestsFromTestCase(TestMathMethod_add))
        # 具体到整个用例点
        from Day10_requests import Demo2_unittest_TestCase
        suite.addTest(loader.loadTestsFromModule(Demo2_unittest_TestCase))
        runner = unittest.TextTestRunner()
        runner.run(suite)












