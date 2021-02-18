# FileName: httpRequestTest.py
# Date：2021-02-05 15:11
# Author：CP3


from Utils.requestUtil import RequestUtil
from Day11.TestParameters.GetData import GetData
from Day12.TestCase.GetUserInfoApiTest_parameterizeByDDT import getUserInfoTestCase
import unittest
import sys

"""
测试用例之间的相似度很高，这个时候应该考虑用参数化的方式去做
测试用例之间相似的点：1.请求路径 2.请求参数 3.断言（预期结果）
"""


class loginTestCase(unittest.TestCase):
    def __init__(self, item, methodName):
        super(loginTestCase,self).__init__(methodName)
        self.item = item
        self._type_equality_funcs = {}

    def testLoginApi(self):
        if self.item["module"] == "Login":
            try:
                # url, method, data=None, json=None, cookies=None, headers=None
                result = RequestUtil().requestMethod(url=self.item["url"], method=self.item["method"],
                                                     json=eval(self.item["data"]),
                                                     headers={"Content-Type": "application/json;charset=UTF-8"})
                if "code" in result.json():
                    self.assertEqual(first=self.item["expected"], second=result.json()["code"],
                                     msg="返回数据与期望值不一致，期望值：{0}，返回数据：{1}".format(self.item["expected"],
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
        else:
            return

