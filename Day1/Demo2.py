a = '128'
b = 128.8888
c = False
d = 'Hello'
print(type(a),type(b),type(c),type(d))
a = int(a)
b = int(b)
c = int(c)
# d = int(d) invalid literal for int() with base 10: 'Hello' 一定要是数字串才能转换成数字类型，否则会报错
print(type(a),type(b),type(c),type(d))




