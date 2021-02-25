# FileName: geiData
# Date：2021-02-19 11:39
# Author：CP3

import pandas as pd


class getData:
    Authorization = None

    @staticmethod
    def getData(sheet_name, key):
        df = pd.read_excel(io=r"D:\PythonWorkspace\Demo1\API_AUTO\test_data\TestData.xlsx", sheet_name=sheet_name)
        return df



if __name__ == '__main__':
    print(getData.getData(sheet_name="public", key="email"))
