# @Author: Chris Paul
# @Time: 2021/01/25 22:27
# @File: Day5_homework.py
o_sum = 0
j_sum = 0
# 输出1到100偶数之和
for i in range(0,100,2):
    o_sum += i
# 输出1到100奇数之和
for i in range(1,100,2):
    j_sum += i

def calSum(to):
    o_sum = 0
    ji_sum = 0
    for i in range(0,to,2):
        o_sum += i
    for i in range(1,to,2):
        ji_sum += i
    return {"ou":o_sum,"ji":ji_sum}

if __name__ == '__main__':
    print("0-100的偶数之和：{0}\n0-100奇数之和：{1}".format(calSum(101).get("ou"),calSum(101).get("ji")))

