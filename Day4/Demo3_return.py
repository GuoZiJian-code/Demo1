# @Author: Chris Paul
# @Time: 2021/01/19 23:02
# @File: Demo3_return.py
def _caculateSum(start, end, step=1):
    sum = 0
    for i in range(start, end, step):
        sum += i
    # print("1-100总和：{0}".format(sum))
    return sum + 100
# 当我们调用这个函数的时候才会进行返回值
result = _caculateSum(1,100) + 100
print(result)





