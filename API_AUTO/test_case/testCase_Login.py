# FileName: testCase_Login
# Date：2021-02-19 15:52
# Author：CP3

import unittest
from API_AUTO.utils.requestUtil import requestAPI
from API_AUTO.test_data.getData import getData


class testCase_Login(unittest.TestCase):
    def __init__(self):
        pass

    def setUp(self):
        pass

    def test_LoginAPI(self, item):
        if item["module"].lower() == "login":
            try:
                headers = {}
                if hasattr(getData, "Authorization"):
                    headers = {"Authorization": getattr(getData, "Authorization")}
                result = requestAPI.requestAPI(method=item["method"], url="back/entrance/_getTokenByLogin",
                                               data=eval(item["data"]), headers=headers)
                print(result.json())
                self.assertEqual(item["expected"], second=result.json().get("code"),
                                 msg="预期值：{0}，实际值：{1}".format(item["expected"], result.json().get("code")))
            except Exception as e:
                print(e)
            except ValueError as e:
                print(e)

    def tearDown(self):
        pass
