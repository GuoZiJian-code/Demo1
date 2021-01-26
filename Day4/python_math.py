# @Author: Chris Paul
# @Time: 2021/01/20 22:31
# @File: python_math.py

def add(*args):
    result = 0
    for i in args:
        result += i
    return  result

def add_sum(j,i=1,k=1):
    sum = 0
    for item in range(i,j,k):
        sum += item
    return sum