# @Author: Chris Paul
# @Time: 2021/02/24 23:06
# @File: Demo1_numpy.py.py

import pandas as pd
from API_AUTO.utils.pathUtil import pathUtils

# 创建一个Excel文件
# df = pd.DataFrame({'ID':[1,2,3],'Name':["Paul","Chris","Geo"]})
# df = df.set_index(keys="ID")
# print(df)
# df.to_excel(excel_writer="text.xlsx")
# print("Done!")

# 读取一个Excel
df = pd.read_excel(io=pathUtils.pathApi(file_paths=["test_data", "TestData.xlsx"]), index_col="caseID").ix[0,0]
print(df)


