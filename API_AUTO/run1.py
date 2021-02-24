# @Author: Chris Paul
# @Time: 2021/02/18 22:52
# @File: run1.py

from API_AUTO.utils.ExcelUtil import do_Excel
from API_AUTO.utils.requestUtil import requestAPI
from API_AUTO.test_data import getData


def run(test_data, sheet_name):
    for item in test_data:
        print("现在执行的用例为：{0}功能点的 {1} 用例".format(item["module"], item["description"]))
        headers = {}  # 给headers设置初始化参数，防止requests的headers未定义
        if hasattr(getData,
                   "Authorization"):  # 当Authorization存在数据时，则把getData中的Authorization添加到headers中的Authorization中去作为凭证
            headers = {"Authorization": getattr(getData, "Authorization")}
        result = requestAPI.requestAPI(method=item["method"], url=item["url"], json_data=eval(item["data"]),
                                       headers=headers)
        # column_name, case_id, write_value
        do_Excel(sheet_name=sheet_name).writeExcel(column_name="result", row_name=item["caseID"],
                                                   write_value=result.text)
        # 当result中存在idToken则利用反射将idToken赋值给Authorization
        if result.json().get("idToken"):
            setattr(getData, "Authorization", result.json().get("idToken"))
        print(result.json())


test_data = do_Excel(sheet_name="login").readExcel()
run(test_data, sheet_name="login")
test_data = do_Excel(sheet_name="register").readExcel()
run(test_data, sheet_name="register")
