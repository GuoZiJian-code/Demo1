# FileName: httpRequestTest.py
# Date：2021-02-05 15:11
# Author：CP3

from requests import RequestException
from Utils.requestUtil import RequestUtil
from Day11.TestParameters.GetData import GetData
import unittest
import json
"""
测试用例之间的相似度很高，这个时候应该考虑用参数化的方式去做
测试用例之间相似的点：1.请求路径 2.请求参数 3.断言（预期结果）
"""


class loginTestCase(unittest.TestCase):
    def __init__(self, methodName, requestUrl, requestMethod, requestData, responseExpected):
        super(loginTestCase, self).__init__(methodName)
        self.requestUrl = requestUrl
        self.requestMethod = requestMethod
        self.requestData = requestData
        self.responseExpected = responseExpected

    def testLoginApi(self):
        try:
            print(self.requestUrl, self.requestMethod, self.requestData, self.responseExpected)
            # url, method, data=None, json=None, cookies=None, headers=None
            result = RequestUtil().requestMethod(url=self.requestUrl, method=self.requestMethod, data=self.requestData,
                                                 headers={"Content-Type": "application/json;charset=UTF-8"})
            if "code" in result.json():
                self.assertEqual(first=self.responseExpected, second=result.json()["code"],
                                 msg="返回数据与期望值不一致，期望值：{0}，返回数据：{1}".format(self.responseExpected,
                                                                           result.json()["code"]))
            elif "idToken" in result.json():
                self.assertIsNotNone(result.json()["idToken"],
                                     msg="返回数据与期望值不一致，期望值应有Token，返回数据：{0}".format(result.json()["idToken"]))
                setattr(GetData, "Authenticate", result.json()["idToken"])
        except AssertionError as e:
            print("断言错误，预期结果与实际结果不一致")
            raise e
        except Exception as e:
            print(e)
            raise e


"""
    # 输入正确的账号和密码
    def test_login_Correct_Input(self):
        try:
            # 参数
            loginInfo_Json = {"username": "admin", "password": "000000", "captcha": "12345",
                              "randomStr": "123456"}
            headers = {"Content-Type": "application/json;charset=UTF-8"}
            result = RequestUtil().requestMethod(url=LOGIN_URL,
                                                 method="post", json=loginInfo_Json, headers=headers)
            if result.json()["idToken"]:
                setattr(GetData, "Authenticate", result.json()["idToken"])
            else:
                self.assertIsNotNone(result.json()["idToken"])
            # 预期结果
            self.assertIsNotNone(result.json()["idToken"],
                                 msg="账号密码正确，成功获取idToken，且idToken不为空，获取的idToken={0}".format(result.json()["idToken"]))
        except AssertionError as e:
            print("未返回正确的userVo！目前为空，\n返回结果：{0}，\n异常结果：{1}".format(result.json(), e))
            raise e
        except RequestException as e:
            print("请求异常，请查看请求代码")
            raise e
        except Exception as e:
            print("出现异常情况", e)
            raise e

    # 不输入账号
    def test_login_No_Username(self):
        try:
            # 参数
            loginInfo_Json = {"username":"","password": "000000", "captcha": "12345", "randomStr": "123456"}
            headers = {"Content-Type": "application/json;charset=UTF-8"}
            result = RequestUtil().requestMethod(url=LOGIN_URL,
                                                 method="post", json=loginInfo_Json, headers=headers)
            # 预期结果
            self.assertEqual(40001, result.json()["code"],
                             msg="当未输入账号时候，接口返回code应为40001(int),目前为{0}".format(result.json()["code"]))
        except AssertionError as e:
            print("未返回正确的userVo！目前为空，返回结果：{0}，异常结果：{1}".format(result.json(), e))
            raise e
        except RequestException as e:
            print("请求异常，请查看请求代码")
            raise e
        except Exception as e:
            print("出现异常情况", e)
            raise e

    # 不输入密码
    def test_login_No_Password(self):
        try:
            # 参数
            loginInfo_Json = {"username": "admin", "captcha": "12345", "randomStr": "123456"}
            headers = {"Content-Type": "application/json;charset=UTF-8"}
            result = RequestUtil().requestMethod(url=LOGIN_URL,
                                                 method="post", json=loginInfo_Json, headers=headers)
            # 预期结果
            self.assertEqual(40001, result.json()["code"],
                             msg="当未输入密码时候，接口返回code应为40001(int),目前为{0}".format(result.json()["code"]))
        except AssertionError as e:
            print("未返回正确的userVo！目前为空，返回结果：{0}，异常结果：{1}".format(result.json(), e))
            raise e
        except RequestException as e:
            print("请求异常，请查看请求代码")
            raise e
        except Exception as e:
            print("出现异常情况", e)
            raise e

    # 输入错误密码
    def test_login_ErrorPassword(self):
        try:
            # 参数
            loginInfo_Json = {"username": "admin", "password": "123456", "captcha": "12345",
                              "randomStr": "123456"}
            headers = {"Content-Type": "application/json;charset=UTF-8"}
            result = RequestUtil().requestMethod(url=LOGIN_URL,
                                                 method="post", json=loginInfo_Json, headers=headers)
            # 预期结果
            self.assertEqual(40301, result.json()["code"], msg=result.json()["message"])
        except AssertionError as e:
            print("未返回正确的userVo！目前为空，返回结果：{0}，异常结果：{1}".format(result.json(), e))
            raise e
        except RequestException as e:
            print("请求异常，请查看请求代码")
            raise e
        except Exception as e:
            print("出现异常情况", e)
            raise e

    def tearDown(self):
        print("每次执行用例结束后执行（每条用例都执行）\nAUTHENTICATE：{0}".format(getattr(GetData, "Authenticate")))



# 获取用户信息：1.已登录获取用户信息 2.未登录直接获取用户信息



class getUserInfoTestCase(unittest.TestCase):
    def test_getUserInfoWithAuthorization(self):
        try:
            if not hasattr(GetData, "Authenticate"):
                raise ValueError("参数异常，authorization为空值")
            else:
                headers = {"Authorization": "Bearer {0}".format(getattr(GetData, "Authenticate"))}
                result = RequestUtil().requestMethod(method="Get", url=GET_USER_INFO_URL,
                                                     headers=headers,
                                                     cookies={"theme": "#409EFF",
                                                              "vue_admin_template_token	": getattr(GetData,
                                                                                                      "Authenticate")})

                self.assertIsNotNone(result.json()['userVo'])
        except AssertionError as e:
            print("未返回正确的userVo！目前为空，返回结果：{0}，异常结果：{1}".format(result.json(), e))
            raise e
        except RequestException as e:
            print("请求异常，请查看请求代码")
            raise e
        except Exception as e:
            print("出现异常情况", e)
            raise e

    def test_getUserInfoWithoutAuthorization(self):
        try:
            result = RequestUtil().requestMethod(method="Get", url=GET_USER_INFO_URL,
                                                 cookies={"theme": "#409EFF"})
            self.assertIsNotNone(result.json()['userVo'])
        except AssertionError as e:
            print("未返回正确的userVo！目前为空，返回结果：{0}，异常结果：{1}".format(result.json(), e))
            raise e
        except RequestException as e:
            print("请求异常，请查看请求代码")
            raise e
        except KeyError as e:
            print("未返回正确的userVo！目前为空，返回结果：{0}，异常结果：{1}".format(result.json(), e))
            raise e
        except Exception as e:
            print("出现异常情况", e)
            raise e
            
"""
