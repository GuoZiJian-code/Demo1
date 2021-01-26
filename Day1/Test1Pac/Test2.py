# list1 = ['杨超越','杨吵吵','超越崽',100,99.9]
# print(list1[1:])
# # List列表添加
# girls = ['杨超越', '超越🐏', '超越崽']
# # while True:
# #     name = input('请输入好看的女生名字：')
# #     if name == 'quit':
# #         break;
# #     girls.append(name)
# # print(girls)
# print(list1)
# print(girls)
# list1.extend(girls)
# print(list1)
# girls.insert(0,'yangchaoyue')
# print(girls)

import random
random_lits = []
# for i in range(10):
#     ran = random.randint(1,20)
#     if(ran not in random_lits):
#         random_lits.append(ran)
# print(random_lits)
i = 0
while i<10:
    ran = random.randint(1,20)
    if (ran not in random_lits):
        random_lits.append(ran)
        i += 1
print(random_lits)
maxNum = random_lits[2]
for ran in random_lits:
    if ran > maxNum:
        maxNum = ran
print('最大数'+ maxNum)