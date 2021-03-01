# author:ChriPaul
# file:Demo1_pandas.py.py
# time:2021/02/23

import pandas as pd
from API_AUTO.utils.pathUtil import pathUtils

df = pd.read_excel(io=(pathUtils.pathApi(file_paths=["test_data","TestData_Parameterist.xlsx"])),sheet_name="TestData")
print(df)

df['等级'][df['名字']=='圣甲狂战'] +=1
print(df)
df.to_excel('1.xlsx',sheet_name="Test1",index=False,header=True)

