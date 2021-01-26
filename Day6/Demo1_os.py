# @Author: Chris Paul
# @Time: 2021/01/25 23:03
# @File: Demo1_os.py.py
import os

"""
# 路径获取1
path1 = os.getcwd()
print("获取到的当前路径：{0}".format(path1))  # 当前文件的工作目录，不是获取当前文件的路径  result:获取到的当前路径：D:\pythonWorkspace\Demo1\Day6\Demo1_os.py

# 路径获取2
path2 = os.path.realpath(__file__)  # __file__：python内的静态变量，表示的是当前文件的本身
print("获取到的当前路径：{0}".format(path2))  # 获取到的当前路径：D:\pythonWorkspace\Demo1\Day6\Demo1_os.py


# 路径拼接1
path3 = os.getcwd()+r"/Btest"
# os.mkdir(path3)
# os.rmdir(path3)
path4 = os.path.join("Atest","Atest-1")
print(path4)
os.mkdir(path4)
"""

# 判断是文件还是目录的方法
os.path.isfile(__file__)
print(os.path.isfile(__file__))  # true
print(os.path.isfile(os.getcwd()))  # false
# 判断文件是否存在
print(os.path.exists(__file__))  # true
print(os.path.exists(os.path.join(os.getcwd(),"Demo2.py")))  # false
# 罗列出当前路径下所有的文件和目录
print(os.listdir(os.getcwd()))
# 给定一个路径，请打印出所有的路径（知道这个路径下没有目录位置）
print(os.getcwd()) # D:\pythonWorkspace\Demo1\Day6


