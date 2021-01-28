# @Author: Chris Paul
# @Time: 2021/01/28 21:13
# @File: Demo2_homework-2.py

# [9,1,52,30,64,94,11,100]
# 使用冒泡排序对其进行排序
# 要循环的次数为要排序列表的长度，因此要在外层控制，然后内层循环控制她每次要走的多少次，每次都从头开始进行排序
_list = [9,1,52,30,64,94,11,100]
for i in range(1,len(_list)):
    for j in range(0,len(_list)-1):
        if _list[j] > _list[j+1]:
            _list[j],_list[j+1] = _list[j+1],_list[j]
print(_list)














