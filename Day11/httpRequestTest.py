# FileName: httpRequestTest.py
# Date：2021-02-05 15:11
# Author：CP3

"""
    1.针对Utils.requestUtil类做作业
    2.访问铝合金的登陆接口和获取用户信息接口进行测试
    3.针对登陆，正常输入，不输入账号，不输入密码，输入错误密码，
      获取用户信息：1.已登录获取用户信息 2.未登录直接获取用户信息
    4.使用任何一种用例加载执行用例
    5.生成HTML的测试报告
"""

from Utils.requestUtil import RequestUtil
import unittest


class loginTestCase(unittest.TestCase):
    # 输入正确的账号和密码
    def test_login_Correct_Input(self):
        loginInfo_Json = {"username": "admin", "password": "000000", "captcha": "12345", "randomStr": "123456"}
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        result = RequestUtil().requestMethod(url="http://polybzh.julytech.cn/back/authenticate",
                                             method="post", json=loginInfo_Json, headers=headers)
        # 预期结果
        self.assertIsNotNone(result.json()["idToken"],
                             msg="账号密码正确，成功获取idToken，且idToken不为空，获取的idToken={0}".format(result.json()["idToken"]))

    # 不输入账号
    def test_login_No_Username(self):
        loginInfo_Json = {"password": "000000", "captcha": "12345", "randomStr": "123456"}
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        result = RequestUtil().requestMethod(url="http://polybzh.julytech.cn/back/authenticate",
                                             method="post", json=loginInfo_Json, headers=headers)
        self.assertEqual(40001, result.json()["code"],
                         msg="当未输入密码时候，接口返回code应为40001(int),目前为{0}".format(result.json()["code"]))

    # 不输入密码
    def test_login_No_Password(self):
        loginInfo_Json = {"admin": "admin", "captcha": "12345", "randomStr": "123456"}
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        result = RequestUtil().requestMethod(url="http://polybzh.julytech.cn/back/authenticate",
                                             method="post", json=loginInfo_Json, headers=headers)
        self.assertEqual(40001, result.json()["code"],
                         msg="当未输入密码时候，接口返回code应为40001(int),目前为{0}".format(result.json()["code"]))

    # 输入错误密码
    def test_login_ErrorPassword(self):
        loginInfo_Json = {"username": "admin", "password": "123456", "captcha": "12345", "randomStr": "123456"}
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        result = RequestUtil().requestMethod(url="http://polybzh.julytech.cn/back/authenticate",
                                             method="post", json=loginInfo_Json, headers=headers)
        self.assertEqual(40301, result.json()["code"], msg=result.json()["message"])


"""
获取用户信息：1.已登录获取用户信息 2.未登录直接获取用户信息
"""


class getUserInfoTestCase(unittest.TestCase):

    def getUserInfoWithAuthorization(self):
        pass
