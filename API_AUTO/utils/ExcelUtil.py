# @Author: Chris Paul
# @Time: 2021/02/18 23:26
# @File: ExcelUtil.py

from openpyxl import load_workbook

class do_Excel:
    def __init__(self,Excel_filename,sheetName):
        self.Excel_filename = Excel_filename
        self.sheetName = sheetName

    def readExcel(self):
        workbook = load_workbook(filename=self.Excel_filename)
        sheet = workbook[self.sheetName]
        for item in range[2, sheet.max_row]