# @Author: Chris Paul
# @Time: 2021/02/25 19:47
# @File: loggingTest.py

import logging
import time


# logger = logging.getLogger("API_AUTO")
# logging.basicConfig(filename="loggerTest.log",level=logging.DEBUG,format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt="%a, %d %b %Y %H:%M:%S",filemode='w')
# logger.addHandler(logging.StreamHandler())
# logger.debug("这是一个DEBUG")

logger = logging.getLogger("API_AUTO")
logger.setLevel(logging.DEBUG)
# 设置输出格式
formatter = logging.Formatter(fmt='Time : %(asctime)s - %(levelname)s级别-%(filename)s文件的[line:%(lineno)d行]-%(name)s-日志信息 : %(message)s')
# 创建输出渠道
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
# 往logger里面添加Handler
logger.addHandler(streamHandler)
logger.debug("哈哈哈哈")

