# @Author: Chris Paul
# @Time: 2021/02/18 23:26
# @File: ExcelUtil.py

from openpyxl import load_workbook
from API_AUTO.utils.doConfigUtil import doConfigUtil


class do_Excel:
    def __init__(self, sheet_name,
                 workbook=load_workbook
                     (filename=doConfigUtil.readConfig(filename="E:\PyProject\Demo1\API_AUTO\ConfigFile\TestConfig.conf",
                                                      section="Excel", option="path")),
                 excel_filename=
                 doConfigUtil.readConfig(filename="E:\PyProject\Demo1\API_AUTO\ConfigFile\TestConfig.conf",
                                         section="Excel", option="path")):

        self.workbook = workbook
        self.sheet_name = sheet_name
        self.excel_filename = excel_filename

    def readExcel(self):
        sheet = self.workbook[self.sheet_name]
        result_list = []
        for i in range(2, sheet.max_row + 1):
            result_item = {}
            for j in range(1, sheet.max_column + 1):
                result_item[sheet.cell(1, j).value] = sheet.cell(i, j).value
            result_list.append(result_item)
        return result_list



if __name__ == '__main__':
    print(do_Excel().readExcel(sheet_name="Test"))
