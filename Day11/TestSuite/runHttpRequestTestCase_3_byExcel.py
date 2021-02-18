# author: ChriPaul
# file: runHttpRequestTestCase_byExcel_ddt.py
# time: 2021 / 02 / 10
import time
import unittest
import HTMLTestReportCN
from Day11.TestCase.httpRequestTest_2_parameterize import loginTestCase
from Utils.doExcel import doExcelUtils


class runHttpRequestTestCase_3_byExcel:
    if __name__ == '__main__':
        """
            使用Excel进行参数化，并请求测试TestCase
            使用注意点：当使用此Excel的时候，会出现取出的数据均是str类型的问题，所以要用到eval(。。。)进行转换成原本的字符串，否则dict也会变成str
        """
        dataList = doExcelUtils(fileName="C:\\Users\\ChriPaul\\Desktop\\TestData.xlsx", sheetName="Test").readExcel()
        suite = unittest.TestSuite()
        for item in dataList:
            suite.addTest(loginTestCase(methodName="testLoginApi", requestUrl=item["url"],
                                        requestMethod=item["method"],
                                        requestData=eval(item["data"]), responseExpected=item["expected"]))

        with open(file="D:\PythonWorkspace\Demo1\Day11\TestReport\登录以及获取用户信息接口测试{0}.html".format(
                time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())), mode="wb") as file:
            HTMLTestReportCN.HTMLTestRunner(stream=file, verbosity=2, title="登录接口测试报告",
                                            description="登录接口测试报告", tester="郭子健").run(suite)


"""
# 打开Excel
        wb = load_workbook(filename="C:\\Users\\ChriPaul\\Desktop\\TestData.xlsx")
        # 定位Sheet
        sheet = wb["Test"]  # 传表单名
        cellValue = sheet.cell(1, 1).value  # 定位并获取值
"""
