# @Author: Chris Paul
# @Time: 2021/02/18 23:21
# @File: testCase_Register.py

import unittest
from API_AUTO.test_data.getData import getData
from API_AUTO.utils.requestUtil import requestAPI


class testCase_Register(unittest.TestCase):
    def __init__(self):
        pass

    def setUp(self):
        pass

    def test_RegisterAPI(self, item):
        if item["module"] == "UserRegister":
            try:
                if not hasattr(getData, "Authentication"):
                    raise Exception("参数异常，无Authentication")
                else:
                    headers = {"Authorization": getattr(getData, name="Authorization"),
                               "Accept": "application/json, text/plain, */*"}
                result = requestAPI.requestAPI(method=item["method"], url="back/api/users", data=eval(item["data"]), headers=headers)

            except Exception as e:
                print(e)
        pass

    def tearDown(self):
        pass
