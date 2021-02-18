# FileName: httpRequestTest.py
# Date：2021-02-05 15:11
# Author：CP3


from requests import RequestException

from Utils.requestUtil import RequestUtil
from Day11.TestParameters.GetData import GetData
from ddt import ddt, data
from Day12.doExcel import doExcelUtils

import unittest
import sys
"""
测试用例之间的相似度很高，这个时候应该考虑用参数化的方式去做
测试用例之间相似的点：1.请求路径 2.请求参数 3.断言（预期结果）
"""


class getUserInfoTestCase(unittest.TestCase):
    def __init__(self, item, methodName):
        super(getUserInfoTestCase,self).__init__(methodName)
        self.item = item
        self._type_equality_funcs = {}

    def test_getUserInfoApi(self):
        if self.item["module"] == 'getUserInfo':
            try:
                if not hasattr(GetData, "Authenticate"):
                    raise ValueError("参数异常，authorization为空值")
                else:
                    if self.item["description"] == "No_idtoken":
                        cookies = {}
                        headers = {}
                    else:
                        cookies = {"theme": "#409EFF", "vue_admin_template_token	": getattr(GetData, "Authenticate")}
                        headers = {"Authorization": "Bearer {0}".format(getattr(GetData, "Authenticate"))}

                    result = RequestUtil().requestMethod(method="Get", url=self.item["url"],
                                                         headers=headers,
                                                         cookies=cookies)
                    if self.item["description"] == "No_idtoken":
                        self.assertEqual(self.item["expected"], result.json()["code"])
                    else:
                        self.assertIsNotNone(result.json()['userVo'])
            except AssertionError as e:
                print("未返回正确的userVo！目前为空，返回结果：{0}，异常结果：{1}".format(result.json(), e))
                raise e
            except KeyError as e:
                print("返回数据无所需校验字段！目前返回：{0}".format(result.json()))
                raise e
            except RequestException as e:
                print("请求异常，请查看请求代码")
                raise e
            except Exception as e:
                print("出现异常情况", e)
                raise e
