"""
sum = 0
L = [5,6,7,3,7]
for item in L:
    sum += item
print('总和为{0}'.format(sum))
"""
d = {"age":18,"name":"郭子健"}
print(d.values())  # 获取字典里面所有的value值
for item in d:
    print(item)  # 只获取了key
    """要获取value的方法"""
    print(d[item])  # 方法一
print("------------------------------")
# 方法二
print(type(d.values()))  # dict_values 字典值数据类型
for item in d.values():
    print(item)

