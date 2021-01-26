# 循环 for while 关键字
# python for循环语法
# for item in Iterator（某个数据类型：字符串、元组、列表、字典、集合等）:
#     代码块
# in为成员运算符：in & not in
# for循环的循环次数，由数据的元素个数进行决定
"""
使用场景：
1.用来控制循环次数
2.遍历这个Iterator的数据组并赋值给item
"""
s = 'hello'
l = [1,2,3]
d = {"age":18,"name":"郭子健"}
for item in s:  # for循环:1用于遍历s中的元素，然后赋值给item
    print("**66@@") # 遍历5次
for item in l:
    print(item)
for item in d:
    print(d[item])

