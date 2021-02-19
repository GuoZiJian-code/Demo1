# FileName: testCase_Login
# Date：2021-02-19 15:52
# Author：CP3

import unittest
from API_AUTO.utils.requestUtil import requestAPI

class testCase_Login(unittest.TestCase):
    def __init__(self):
        pass
    def setUp(self):
        pass

    def test_LoginAPI(self, item):
        if item["module"].lower() == "login":
            try:
                result = requestAPI.requestAPI(method=item["method"],url="back/entrance/_getTokenByLogin",option="gchn_url",
                                      data=eval(item["data"]))
                result.json()["status"]
            except Exception as e:
                print(e)
            except ValueError as e:
                print(e)

    def tearDown(self):
        pass


