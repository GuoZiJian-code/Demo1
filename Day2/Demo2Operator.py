"""
运算符 常用5大类
"""
# 算数运算符 + - * / %
# 取余运算（模运算） 判断某个数是偶数还是奇数的时候
a = 10
print(a % 3)  # 1
# 赋值运算符 = += -= *=
a = 10  # 赋值运算
print(a)
a += 1  # 11
print(a)
a -= 2  # 9
print(a)
a *= 2  # 18
print(a)
# 比较运算符 > < >= <= == != 返回的值是布尔值
print('GET' == 'get')  # False
print('GET'.lower() == "get")  # True
# 逻辑运算符 and or 拓展： not 返回结果是布尔值
a = 10
b = 5
print(a > 11 and a > 6 and a > 1)  # False 有其中一个是False那就返回False
print(a > 11 or a > 6)  # True 有其中一个为True那就返回True
# 成员运算符 in 和 not in 返回值也是布尔值
s = 'hello'
print('o' in s)  # True
print('o' not in s)  # False
_list = [1,2,3]
print(1 not in _list)  # False
print(1 in _list)  # True
_dist = {"name":"zhangSan","age":40}  # 字典判断的是这个Key在不在字典中，Value不去判断
print("zhangSan" in _dist)  # False
print("name" in _dist)  # True












