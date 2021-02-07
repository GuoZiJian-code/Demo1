# FileName: runHttpRequestTestCase
# Date：2021-02-07 13:46
# Author：CP3

import unittest
import os
import HtmlTestRunner
from Day11.TestRequest import httpRequestTest


class runHttpRequestTestCase(httpRequestTest):
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromModule(httpRequestTest))
    try:
        runner = HtmlTestRunner.HTMLTestRunner(output="E:\\PyProject\\Demo1\\TestReport", verbosity=2,
                                               combine_reports=True,report_name="登录以及获取用户信息接口测试")
        runner.run(suite)
    except FileNotFoundError as e:
        os.mkdir("E:\\PyProject\\Demo1\\TestReport")
