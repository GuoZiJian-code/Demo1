# @Author: Chris Paul
# @Time: 2021/01/20 22:21
# @File: Demo1_import1.py.py
# 怎么用Python的库？
"""
第一种情况：自己写的库，怎么导入？
"""
from Day4 import python_math
print(result =python_math.add_sum(100))


"""
第二种情况：Python自带的或者是后面安装的第三方库，怎么引用？
1.import
2.from ... import
"""
# import email.mime.base
# import myTestLib.python_math
# from myTestLib import python_math
# from myTestLib.python_math import  add_sum
# print(add_sum(1,2,3))