import random
# s1 = 'abc'
# s2 = "abc"
# s3 = '''
# abc
# '''
# print(s1 == s2) #比较内容
# print(s1 is s2) #比较地址
# print(s2 == s3)
# print(s2 is s3)
# print(id(s1),id(s2),id(s3))
# s1 = input('set:')
# s2 = input('set:')
# print(s1 == s2)
# print(s1 is s2)

# str = 'hello world'
# print(str[-1:-6:-1])
# print(str[0:5:1])
# print(str[::-1])
# print('llo' in str)
# print(str[-7:-10:-1])
# print(str[2:8:1])
# print(str[::2])

# 验证码
# realCode = ''
# str = 'QWERTYUIOASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm'
# for i in range(4):
#     ran = random.randint(1, len(str) - 1)
#     realCode += str[ran]
# print(realCode)
# userInputCode = input('请输入验证码：')
# if userInputCode.lower() == realCode.lower():
#     print('验证成功')
# else :
#     print('验证失败')

str = r'los\asdas\t\1\`\` angeles clippers champions'
print(str)
position = str.find('e',0)
print(position)
position = str.find('e',position+1)


url = r'https://www.baidu.com/img\bd_logo1.png'
# position = url.rfind('\\')
# print(position)
# imgPath = url[position+1:]
# print(imgPath)
# print(imgPath.encode('utf-8'))
# print(url.endswith('.png'))
# # print(url.startswith('https://'))
# url = 'adasdas'
# print(url.isalpha())
# url = '1213412a412'
# print(url.isdigit())
# result = url.split('a')

# str1 = 'they are student'
# str2 = 'asdvcx'
# for i in str2:
#     str1 = str1.replace(i,'')
# print(str1)
#
#
# word = input('输入单词：')
# for i in range(len(word)):
#     if word.islower():
#         print('不喜欢,大写')
#         break
#     else:
#         if i < len(word)-1 and word[i] == word[i+1]:
#             print('不喜欢，叠词')
#             break
# else:
#     print('喜欢'+word)


brands = ['hp','mac','lenovo','HASEEN']
len = len(brands)
i = 0
while i < len:
    if 'mac' in brands[i]:
        del brands[i]
        len-=1
    i+=1
print(brands)