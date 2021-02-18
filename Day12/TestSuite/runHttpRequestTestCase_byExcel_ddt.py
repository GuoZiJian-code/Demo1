# author: ChriPaul
# file: runHttpRequestTestCase_byExcel_ddt.py
# time: 2021 / 02 / 10
import time
import unittest
import HTMLTestReportCN
from Day12.TestCase.testAPI import TestAPI
from Day12.doExcel import doExcelUtils

test_data = doExcelUtils(fileName="C:\\Users\\Administrator\\Desktop\\TestData.xlsx", sheetName="Test").readExcel()


# unittest+ddt+Excel
# 使用unittest+ddt的框架有个坑点，由于是没有传参的，所以只能用TestLoader进行加载测试用例
class runHttpRequestTestCase_3_byExcel:
    """
        使用ddt里的@data和@unpack对Excel获取到的数据进行拆分并使用
    """
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestAPI))
    with open(file="D:\pythonWorkspace\Demo1\Day11\TestReport\登录以及获取用户信息接口测试{0}.html".format(
            time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())), mode="wb") as file:
        HTMLTestReportCN.HTMLTestRunner(stream=file, verbosity=2, title="登录接口测试报告",
                                        description="登录接口测试报告", tester="CP3").run(suite)
