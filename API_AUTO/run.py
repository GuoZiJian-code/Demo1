# @Author: Chris Paul
# @Time: 2021/02/18 22:52
# @File: run.py

import HTMLTestReportCN
import unittest
from API_AUTO.test_case.testCase_requestAPI import testCase_RequestAPI
from API_AUTO.utils.pathUtil import pathUtils

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(testCase_RequestAPI))
with open(file=pathUtils.pathApi(file_paths=["test_report","test_report_requestAPI.html"]),mode="wb") as file:
    run = HTMLTestReportCN.HTMLTestRunner(stream=file,title="requestAPI接口测试",description="requestAPI接口测试",tester="CP3").run(suite)

