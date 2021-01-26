# @Author: Chris Paul
# @Time: 2021/01/21 22:29
# @File: Demo2_File1.py
"""
mode打开这个文件的模式
r（只读） w（只写） a（追加）
r+ w+ a+
rb rb+ wb wb+ ab ab+：针对二进制文件的读取，b为binary的意思

testFile = open("./Test.txt",mode='r+')
res = testFile.read(5)
testFile.write("Write")
print(res)
"""
# 1.mode="w"时，可写模式，不可读，若无此文件，则新增，若有此文件则清空重写，报错：io.UnsupportedOperation: not readable,写的话，注意就是这个是把文件清空了崽去写，非常危险
# 2.testFile.write("6666")
#   mode="r"时，可读模式，不可写，file.write("xxx")，报错：io.UnsupportedOperation: not writable
# 3.mode="r+"时，可读可写，如果需要写入字符，会根据光标进行选择开始输入的位置，比如我读完整个文件再写，那么光标在最后，所以会把文本加在文件最后，如果我先写后读光标就在第一位，因此就写在第一个字符
#   选择只读取前五个字符，那么也会在文末进行输入字符，原因：进行完一次读取操作后，光标自动就挪到最后了
# 4.如果需要写入中午，则需要指定编码格式
"""
testFile1 = open("./Test.txt",mode="r",encoding="utf-8")
res = testFile1.read()
print(res)
"""
# 5.最好读写两步操作分开，不然会造成混乱和报错
# 6.mode="w+"时，可读可写模式，若无此文件，则新增文件，若有此文件则清空重写
testFile = open("./Test2.txt",mode="w+",encoding="utf-8")
testFile.write("哈哈哈哈")
