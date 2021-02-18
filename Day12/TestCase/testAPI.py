# author:ChriPaul
# file:testAPI.py
# time:2021/02/14

import unittest

from ddt import ddt, data

from Day12.TestCase import GetUserInfoApiTest_parameterizeByDDT, LoginApiTest_parameterizeByDDT
from Day12.doExcel import doExcelUtils

test_data = doExcelUtils(fileName="C:\\Users\\Administrator\\Desktop\\TestData.xlsx", sheetName="Test").readExcel()


@ddt
class TestAPI(unittest.TestCase):
    @data(*test_data)
    def testApi(self, item):
        if str(item["module"]).lower() == "login":
            LoginApiTest_parameterizeByDDT.loginTestCase(item=item, methodName="testLoginApi").testLoginApi()
        elif str(item["module"]).lower() == "getuserinfo":
            GetUserInfoApiTest_parameterizeByDDT.getUserInfoTestCase(item=item,
                                                                     methodName="test_getUserInfoApi").test_getUserInfoApi()
