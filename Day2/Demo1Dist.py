"""
使用场景：
字典：一个数据里面，每个数据都是用作不同用途的，这时候用字典来存储
"""
# 字典 符号dist,K-V形式,分隔符为逗号,3.6版本前为无序字典,3.6版本后变成有序字典
# 赋值
a = {
    'name': 'GuoZiJian',
    'age': 22,
    'location': 'GZ'
}
''' 取值：a[所需要取值的Key]或者a.get(所需取值的Key) '''
# 第一种取值 a[所需要取值的Key]
print('第一种：我的名字是{0},今年{1}岁'.format(a['name'], a['age']))
# 第二种取值 a.get(所需取值的Key)
print('第二种：我的名字{0},住在{1}'.format(a['name'], a['location']))
''' 增加：a[所需增加的key]=所需增加的value'''
a['code'] = '1612402702054'
print(a)  # {'name': 'GuoZiJian', 'age': 22, 'location': 'GZ', 'code': '1612402702054'}
''' 删除pop(key)指明删除的值key '''
a_del = a.pop('location')
print(a_del)  # GZ
print(a)  # {'name': 'GuoZiJian', 'age': 22, 'code': '1612402702054'}
''' 修改a['原来已有的Key']=新的value '''
a['location'] = 'GuangZhou'
a['age'] = 23
print(a)  # {'name': 'GuoZiJian', 'age': 23  , 'code': '1612402702054', 'location': 'GuangZhou'}
''' 规范性问题：同一个字典中不应有多个重复的key,可以有，但后期会导致数据有问题，如果真的有的话，会使用该key最后一个值 '''
errorA = {
    'name': '郭子健',
    'age': 18,
    'name': 'CP3'
}
print(errorA['name'])  # CP3


