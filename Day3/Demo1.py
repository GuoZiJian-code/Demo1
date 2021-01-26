import random
num_1 = random.randint(1,9)
num_2 = int (input("请输入你的数字:"))
if num_1 > num_2:
    print("bigger")
elif num_1 < num_2:
    print("less")
else:
    print("equal")


