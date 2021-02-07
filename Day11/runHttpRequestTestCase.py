# FileName: runHttpRequestTestCase
# Date：2021-02-07 13:46
# Author：CP3

import unittest
import os
import HtmlTestRunner
from Day11.TestRequest import httpRequestTest


class runHttpRequestTestCase(httpRequestTest):

    if __name__ == '__main__':
        # 第一种方法，全部用例一起加进去
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        suite.addTest(loader.loadTestsFromModule(httpRequestTest))
        try:
            runner = HtmlTestRunner.HTMLTestRunner(output="E:\\PyProject\\Demo1\\TestReport", verbosity=2,
                                                   combine_reports=True, report_name="登录以及获取用户信息接口测试").run(suite)
        except FileNotFoundError as e:
            os.mkdir("E:\\PyProject\\Demo1\\TestReport")

        # 第二种方法，一个一个加用例，好处就是可以控制执行顺序，坏处就是太麻烦了
        """
        suite = unittest.TestSuite()
        suite.addTest(httpRequestTest.loginTestCase("test_login_Correct_Input"))
        suite.addTest(httpRequestTest.loginTestCase("test_login_ErrorPassword"))
        suite.addTest(httpRequestTest.loginTestCase("test_login_No_Password"))
        suite.addTest(httpRequestTest.loginTestCase("test_login_No_Username"))
        suite.addTest(httpRequestTest.getUserInfoTestCase("test_getUserInfoWithAuthorization"))
        suite.addTest(httpRequestTest.getUserInfoTestCase("test_getUserInfoWithoutAuthorization"))
        try:
            runner = HtmlTestRunner.HTMLTestRunner(output="E:\\PyProject\\Demo1\\TestReport", verbosity=2,
                                                   combine_reports=True, report_name="登录以及获取用户信息接口测试").run(suite)
        except FileNotFoundError as e:
            os.mkdir("E:\\PyProject\\Demo1\\TestReport")
        """
