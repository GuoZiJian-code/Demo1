# @Author: Chris Paul
# @Time: 2021/01/27 11:38
# @File: Demo3_try_except.py
from io import UnsupportedOperation
import os
"""
精确定位到哪个异常，直处理某个错误
try:
    print("这里估计会有一个FileNotFoundError异常")
    file = open("./Demo1_os.py")
    file.write("print()")
except FileNotFoundError :
    print("抓到了FileNotFoundError异常")
except UnsupportedOperation:
    print("抓到了UnsupportedOperation异常")
print("不知道抓捕没抓捕...直接就下班了")
"""
"""
只处理某一个类型的异常
try:
    os.mkdir("Demo1")
except OSError:
    print("有关于OS的异常均进行异常处理")
"""
"""
只要有错误就进行处理
try:
    file = open("./Demo1_os.py")
    file.write("就很尼玛离谱")
except Exception as e:
    print("处理所有异常")
"""
"""
try:
    ...
except:
    ....
finally:
    ....
-----------------------------------------------------------------
try:
    file = open("./Demo1_os.py")
    file.write("就很尼玛离谱")
    file.close()
except Exception as e:
    print("错误为{0}".format(e))
    errorFile = open("Error.txt",mode="a",encoding="utf-8")
    errorFile.write(str(e)+r"\n")
    errorFile.close()
finally:
    print("不管你犯没犯错了，我最后还是会执行")
"""
"""
try:
    ....
except:
    ....
else:
    ....
"""
try:
    file = open("./Demo1_os.py")
    file.close()
except Exception as e:
    print("错误为{0}".format(e))
    errorFile = open("Error.txt",mode="a",encoding="utf-8")
    errorFile.write(str(e)+r"\n")
    errorFile.close()
else:
    print("else的话，当try的代码体正常执行，else的代码体还是会正常执行当try代码提出现异常，else的代码体也会不进行执行")














