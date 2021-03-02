# author:ChriPaul
# file:testCase_requestAPI.py
# time:2021/02/22

import unittest
from API_AUTO.test_data.getData import getData
from API_AUTO.utils.requestUtil import requestAPI
from API_AUTO.utils.ExcelUtil import do_Excel
from API_AUTO.utils.LogUtil import LogUtils
from ddt import ddt, data

test_data = do_Excel(sheet_name="register").readExcel()


@ddt
class testCase_RequestAPI(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_RequestAPI(self, item):
        try:
            headers = {}
            if hasattr(getData, "Authorization"):
                headers["Authorization"] = getattr(getData, "Authorization")
            url = item["data"]
            result = requestAPI.requestAPI(url=item["url"], method=item["method"], json_data=eval(str(item["data"])),
                                           headers=headers)
            LogUtils().info(result.json())
            if result.json().get("idToken"):
                setattr(getData, "Authorization", result.json().get("idToken"))
            do_Excel(sheet_name="register").writeExcel(sheet_name="register",column_name="result",row_name=item["caseID"],write_value=result.text)
            self.assertEqual(item["expected"], result.json().get("code"))
        except AssertionError as e:
            LogUtils().error(msg=e)
        except Exception as e:
            LogUtils().error(msg=e)
            raise e
