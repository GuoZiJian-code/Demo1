 # @Author: Chris Paul
# @Time: 2021/01/18 22:10
# @File: Demo2_function.py
"""def _caculateSum(start, end, step=1):
    sum = 0
    for i in range(start, end, step):
        sum += i
    print("1-100总和：{0}".format(sum))
"""
# 参数位置与传参一致
# _caculateSum(1, 11000, 1)
# 指定参数
# _caculateSum(step=1,start=1,end=50)
# 默认参数必须放在位置参数的后面
# 示例：
# def _caculateSum(Start=1,end,step=1): # 报错：non-default parameter follows default parameter
"""
情景：当调用时，不想传参给已有默认参数的形参
def _caculateSum(start,step=1,end=100):
    print(start,end,step)
_caculateSum(0,end=1000)
"""





