# @Author: Chris Paul
# @Time: 2021/01/26 23:07
# @File: Demo2_homework.py
import os

# 给定一个路径，请打印出所有的路径（知道这个路径下没有目录位置）
def getAllFileInDir(pathStr):
    for item in os.listdir(pathStr):
        if os.path.isfile(os.path.join(pathStr,item)):
            print(os.path.join(pathStr,item))
        else:
            print("文件夹：{0}".format(os.path.join(pathStr,item)))
            getAllFileInDir(os.path.join(pathStr,item))

if __name__ in '__main__':
    getAllFileInDir(r"E:\Learn\1-60")
