# FileName: geiData
# Date：2021-02-19 11:39
# Author：CP3

import pandas as pd
from API_AUTO.utils.pathUtil import pathUtils


class getData:
    Authorization = None

    admin_username = pd.read_excel(io=pathUtils.pathApi(file_paths=["test_data","TestData_Parameterist.xlsx"]),sheet_name="parameters",index_col="Key").loc['admin_username','Value']
    admin_password = pd.read_excel(io=pathUtils.pathApi(file_paths=["test_data","TestData_Parameterist.xlsx"]),sheet_name="parameters",index_col="Key").loc['admin_password','Value']

    real_name = pd.read_excel(io=pathUtils.pathApi(file_paths=["test_data","TestData_Parameterist.xlsx"]),sheet_name="parameters",index_col="Key").loc['real_name','Value']
    email = pd.read_excel(io=pathUtils.pathApi(file_paths=["test_data","TestData_Parameterist.xlsx"]),sheet_name="parameters",index_col="Key").loc["email","Value"]
    mobile = pd.read_excel(io=pathUtils.pathApi(file_paths=["test_data","TestData_Parameterist.xlsx"]),sheet_name="parameters",index_col="Key").loc["mobile","Value"]
    password = pd.read_excel(io=pathUtils.pathApi(file_paths=["test_data","TestData_Parameterist.xlsx"]),sheet_name="parameters",index_col="Key").loc["password","Value"]
    companyId = pd.read_excel(io=pathUtils.pathApi(file_paths=["test_data","TestData_Parameterist.xlsx"]),sheet_name="parameters",index_col="Key").loc["companyId","Value"]
    account = pd.read_excel(io=pathUtils.pathApi(file_paths=["test_data","TestData_Parameterist.xlsx"]),sheet_name="parameters",index_col="Key").loc["account","Value"]

    @staticmethod
    def getData(sheet_name, key):
        df = pd.read_excel(io=r"D:\PythonWorkspace\Demo1\API_AUTO\test_data\TestData.xlsx", sheet_name=sheet_name)
        return df



if __name__ == '__main__':
    print(getattr(getData,"username"))
