# @Author: Chris Paul
# @Time: 2021/02/18 23:26
# @File: ExcelUtil.py

from openpyxl import load_workbook
from API_AUTO.utils.doConfigUtil import doConfigUtil


class do_Excel:
    @staticmethod
    def readExcel(sheet_name, excel_filename=doConfigUtil.readConfig(filename=r"E:\PyProject\Demo1\API_AUTO"
                                                                              "\ConfigFile\TestConfig.conf",
                                                                     section="Excel", option="path")):
        workbook = load_workbook(filename=excel_filename)
        sheet = workbook[sheet_name]
        result_list = []
        for i in range(2, sheet.max_row + 1):
            result_item = {}
            for j in range(1, sheet.max_column + 1):
                result_item[sheet.cell(1, j).value] = sheet.cell(i, j).value
            result_list.append(result_item)
        return result_list

    @staticmethod
    def writeExcel():
        pass
    @staticmethod
    def getCellLocationByValue(sheet_name, value):
        workbook = load_workbook(filename=doConfigUtil.readConfig(filename=r"E:\PyProject\Demo1\API_AUTO"
                                                                           "\ConfigFile\TestConfig.conf",
                                                                  section="Excel", option="path"))
        sheet = workbook[sheet_name]
        for i in range(1,sheet.max_row+1):
            for j in range(1,sheet.max_column+1):
                print(sheet.cell(i, j).value)
                # if sheet.cell(i , j).value == "result":
                #     print(sheet.cell(i, j).value)


if __name__ == '__main__':
    # print(do_Excel().readExcel(sheet_name="Test"))
    do_Excel.getCellLocationByValue(sheet_name="register", value="result")
