# FileName: Demo3_TestSuiteOrTestLoader
# Date：2021-02-05 09:39
# Author：CP3


import unittest
from Day10.Demo2_unittest_TestCase import TestMathMethod_add


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

        # suite = unittest.TestSuite()
        # loader = unittest.TestLoader()
        # 具体到某个功能的用例点
        # suite.addTest(loader.loadTestsFromTestCase(TestMathMethod_add))
        # 具体到整个用例点
        # from Day10 import Demo2_unittest_TestCase
        # suite.addTest(loader.loadTestsFromModule(Demo2_unittest_TestCase))
        # runner = unittest.TextTestRunner() # 可用于打印测试报告
        # runner.run(suite)

        # 生成一个TXT的测试报告（最原始版本）
        def generateTestReportTXT(self):
            suite = unittest.TestSuite()
            loader = unittest.TestLoader()
            suite.addTest(loader.loadTestsFromTestCase(TestMathMethod_add))
            with open("./TestReport.txt", "w+", encoding="UTF-8") as file:
                runner = unittest.TextTestRunner(stream=file, descriptions="这是第一个txt测试用例", verbosity=2)
                runner.run(suite)

        # 生成一个HTML的测试报告（多用）
        def generateTestReportHtml(self):
            suite = unittest.TestSuite()
            loader = unittest.TestLoader()
            suite.addTest(loader.loadTestsFromTestCase(TestMathMethod_add))


if __name__ == '__main__':
    runMath_MethodTestCase = runMath_MethodTestCase()
    runMath_MethodTestCase.generateTestReportTXT()
