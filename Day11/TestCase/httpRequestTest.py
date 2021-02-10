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
from requests import RequestException
from Utils.requestUtil import RequestUtil
from Day11.TestParameters.GetData import GetData
import unittest


# AUTHENTICATE = None
class loginTestCase(unittest.TestCase):
    def setUp(self, login_Url=None, get_userInfo=None):
        self.login_Url = "http://polybzh.julytech.cn/back/authenticate"
        self.get_userInfo = "http://polybzh.julytech.cn/back/userInfo"

    # 输入正确的账号和密码
    def test_login_Correct_Input(self):
        # global AUTHENTICATE
        try:
            loginInfo_Json = {"username": "admin", "password": "000000", "captcha": "12345",
                              "randomStr": "123456"}
            headers = {"Content-Type": "application/json;charset=UTF-8"}
            result = RequestUtil().requestMethod(url=self.login_Url,
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
            loginInfo_Json = {"password": "000000", "captcha": "12345", "randomStr": "123456"}
            headers = {"Content-Type": "application/json;charset=UTF-8"}
            result = RequestUtil().requestMethod(url=self.login_Url,
                                                 method="post", json=loginInfo_Json, headers=headers)
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

    # 不输入密码
    def test_login_No_Password(self):
        try:
            loginInfo_Json = {"username": "admin", "captcha": "12345", "randomStr": "123456"}
            headers = {"Content-Type": "application/json;charset=UTF-8"}
            result = RequestUtil().requestMethod(url=self.login_Url,
                                                 method="post", json=loginInfo_Json, headers=headers)
            self.assertEqual(400012, result.json()["code"],
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
            loginInfo_Json = {"username": "admin", "password": "123456", "captcha": "12345",
                              "randomStr": "123456"}
            headers = {"Content-Type": "application/json;charset=UTF-8"}
            result = RequestUtil().requestMethod(url=self.login_Url,
                                                 method="post", json=loginInfo_Json, headers=headers)
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


"""
获取用户信息：1.已登录获取用户信息 2.未登录直接获取用户信息
"""


class getUserInfoTestCase(unittest.TestCase):
    def test_getUserInfoWithAuthorization(self):
        # global AUTHENTICATE
        try:
            if not hasattr(GetData, "Authenticate"):
                raise ValueError("参数异常，authorization为空值")
            else:
                headers = {"Authorization": "Bearer {0}".format(getattr(GetData,"Authenticate"))}
                result = RequestUtil().requestMethod(method="Get", url="http://polybzh.julytech.cn/back/userInfo",
                                                     headers=headers,
                                                     cookies={"theme": "#409EFF",
                                                              "vue_admin_template_token	": getattr(GetData,"Authenticate")})

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
            result = RequestUtil().requestMethod(method="Get", url="http://polybzh.julytech.cn/back/userInfo",
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
