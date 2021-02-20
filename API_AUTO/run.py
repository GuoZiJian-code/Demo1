# @Author: Chris Paul
# @Time: 2021/02/18 22:52
# @File: run.py

from API_AUTO.utils.ExcelUtil import do_Excel
from API_AUTO.utils.requestUtil import requestAPI


def run(test_data):
    for item in test_data:
        print("现在执行的用例为：{0}功能点的 {1} 用例".format(item["module"], item["description"]))
        result = requestAPI.requestAPI(method=item["method"], url=item["url"], json_data=eval(item["data"]))
        print(result.json())

test_data = do_Excel.readExcel(sheet_name="register")
run(test_data)