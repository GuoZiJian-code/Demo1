# FileName: runHttpRequestTestCase
# Date：2021-02-07 13:46
# Author：CP3

from Day11.TestCase import httpRequestTest_2_parameterize
import HTMLTestReportCN
import time
import unittest


class runHttpRequestTestCase_2(httpRequestTest_2_parameterize):
    login_url = "http://polybzh.julytech.cn/back/authenticate"
    get_userInfo_url = "http://polybzh.julytech.cn/back/userInfo"
    if __name__ == '__main__':
        test_data = [
            {"url": login_url, "method": "POST", "data": {"username": "admin", "password": "000000", "captcha": "12345",
                                                          "randomStr": "123456"}, "expected": {"code": None}},
            {"url": login_url, "method": "POST",
             "data": {"username": "admin", "password": "111111", "captcha": "12345",
                      "randomStr": "123456"}, "expected": {"code": 40301}},
            {"url": login_url, "method": "POST",
             "data": {"username": "admin", "password": "", "captcha": "12345",
                      "randomStr": "123456"}, "expected": {"code": 40001}},
            {"url": login_url, "method": "POST",
             "data": {"username": "", "password": "000000", "captcha": "12345",
                      "randomStr": "123456"}, "expected": {"code": 40001}}
        ]
        loginTest_Suite = unittest.TestSuite()
        for item in test_data:
            loginTest_Suite.addTest(
                httpRequestTest_2_parameterize.loginTestCase(methodName="testLoginApi", requestUrl=item["url"],
                                                             requestMethod=item["method"],
                                                             requestData=item["data"],
                                                             responseExpected=item["expected"]["code"]))
        with open("D:\PythonWorkspace\Demo1\Day11\TestReport\登录以及获取用户信息接口测试{0}.html".format(
                time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())),
                  mode="wb") as TestReportFile:
            runner = HTMLTestReportCN.HTMLTestRunner(stream=TestReportFile, verbosity=2, title="登录接口测试报告",
                                                     description="登录接口测试报告", tester="郭子健"). \
                run(loginTest_Suite)
