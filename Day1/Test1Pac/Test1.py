person="杨超越"
NAME="杨超越"
num1 = 6
code = 464213434.6
print("亲爱的%s,您有%d个快递在邮箱，编码为%.2f"%(NAME,num1,code))
print(str(code)+str(num1))
movie = "皮卡丘"
ticket = 45.922
count = 5
age = 2
message = '乔治说今年{}岁'.format(age)
print(message)
message = '''
电影：{}
票价：{}
人数: {}
总票价：{}
'''.format(movie,ticket,count,float(count*ticket))
print(message)