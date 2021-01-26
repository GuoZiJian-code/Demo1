age = input('请输入年龄：')
# 控制语句 分支分流 循环语句(for、while)
# 判断语句 if.. elif..else  关键字
# if 条件语句{# 比较（> < >= <= == !=） 逻辑（and or） 成员(in、not in)   }
# 1.空数据、空字符串、空列表、空元组、空字典的False  非空数据=True
# 2.可以直接用bool值去控制（倒不如直接写个执行语句）
# 3.一个条件语句里面只能有一个if和else
"""
if age > 18: # 当if后面的语句满足条件 运算结果为True 那他就会执行他的子语句
    print("恭喜你，成年了!")
s = 'hello'
if 'lo' in s:
    print('包含')
s = ''
if s:
    print('为True')
"""
# if 条件语句：
#     子语句
# else: 不能添加条件语句
#     子语句
'''
age = 10
if age > 18:
    print("恭喜你，成年了!")
else:
    print('继续长大')
'''
# if 条件语句:
#   子语句
# elif 条件语句:
#   子语句
# else:
#   子语句
if age.isdigit():
    age = int(age)
    if age >= 18:
        print("成年了")
    elif 0 <= age < 18:
        print("未成年")
    else:
        print("年龄输入有误")
else:
    print("年龄输入有误")
















