# @Author: Chris Paul
# @Time: 2021/02/18 23:26
# @File: ExcelUtil.py

import time
import pandas as pd
from openpyxl import load_workbook
from API_AUTO.utils.doConfigUtil import doConfigUtil
from API_AUTO.utils.pathUtil import pathUtils
from API_AUTO.utils.LogUtil import LogUtils


class do_Excel:
    def __init__(self, sheet_name,
                 workbook=load_workbook
                     (filename=doConfigUtil.readConfig(filename=pathUtils.pathApi(file_paths=["ConfigFile","TestConfig.conf"]),
                                                      section="Excel", option="path")),
                 excel_filename=
                 doConfigUtil.readConfig(filename=pathUtils.pathApi(file_paths=["ConfigFile","TestConfig.conf"]),
                                         section="Excel", option="path")):

        self.workbook = workbook
        self.sheet_name = sheet_name
        self.excel_filename = excel_filename

    def readExcel(self):
        mode = doConfigUtil.readConfig(filename=pathUtils.pathApi(file_paths=["ConfigFile","TestConfig.conf"]),section="MODE",option="mode")
        sheet = self.workbook[self.sheet_name]
        result_list = []
        for i in range(2, sheet.max_row + 1):
            result_item = {}
            for j in range(1, sheet.max_column + 1):
                result_item[sheet.cell(1, j).value] = sheet.cell(i, j).value
            result_list.append(result_item)
        if mode.lower() == "all":
            return result_list
        else:
            final_list = []
            for item in result_list:
                if item["caseID"] in mode:
                    final_list.append(item)
            return final_list

    def getCellLocationByValue(self, value):
        sheet = self.workbook[self.sheet_name]
        for i in range(1, sheet.max_row + 1):
            for j in range(1, sheet.max_column + 1):
                if sheet.cell(i, j).value == value:
                    return {"row": i, "column": j}

    def writeExcel(self, column_name, row_name, write_value):
        value_column_location = self.getCellLocationByValue(column_name)
        value_row_location = self.getCellLocationByValue(row_name)
        if not value_column_location:
            LogUtils().info(msg="Excel中无此列名")
            raise ValueError("Excel中无此列名")
        writeRow = value_row_location.get("row")
        writeColumn = value_column_location.get("column")
        sheet = self.workbook[self.sheet_name]
        sheet.cell(writeRow, writeColumn).value = write_value
        self.workbook.save(
            filename=doConfigUtil.readConfig(filename=pathUtils.pathApi(file_paths=["ConfigFile","TestConfig.conf"]),
                                             section="Excel", option="path"))

    def readExcel_byPandas(self,filepaths,sheet_name):
        return pd.read_excel(io=pathUtils.pathApi(file_paths=filepaths),sheet_name=sheet_name,header=True)

    def writeExcel_byPandas(self):
        pass


if __name__ == '__main__':
    do_Excel(sheet_name="public").writeExcel(column_name="value", row_name="account", write_value="test{}".format(round(time.time() * 1000)))
