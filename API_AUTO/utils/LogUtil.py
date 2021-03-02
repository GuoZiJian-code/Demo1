# @Author: Chris Paul
# @Time: 2021/02/25 20:44
# @File: LogUtil.py

import logging
import datetime
from API_AUTO.utils.pathUtil import pathUtils


class LogUtils:
    def loggerAPI(self, level, msg):
        logger = logging.getLogger("API_AUTO")
        logger.setLevel(logging.DEBUG)
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.DEBUG)
        fileHandler = logging.FileHandler(filename=pathUtils.pathApi(
            file_paths=["learn", "log", "{0}.log".format(datetime.datetime.now().strftime('%Y%m%d'))]),encoding="UTF-8")
        formatter = logging.Formatter(
            fmt='Time:%(asctime)s-level:%(levelname)s-%(filename)s-[line:%(lineno)d]-%(name)s-日志信息 : %(message)s')
        streamHandler.setFormatter(formatter)
        fileHandler.setFormatter(formatter)
        logger.addHandler(streamHandler)
        logger.addHandler(fileHandler)
        if level.upper() == "DEBUG":
            logger.debug(msg)
        elif level.upper() == "INFO":
            logger.info(msg)
        elif level.upper() == "WARNING":
            logger.warning(msg)
        elif level.upper() == "ERROR":
            logger.error(msg)
        elif level.upper() == "CRITICAL":
            logger.critical(msg)
        else:
            logger.debug("输入错误的level,msg:{0}".format(msg))

    def debug(self, msg):
        self.loggerAPI(level="DEBUG", msg=msg)

    def info(self, msg):
        self.loggerAPI(level="info", msg=msg)

    def warning(self, msg):
        self.loggerAPI(level="warning", msg=msg)

    def error(self, msg):
        self.loggerAPI(level="error", msg=msg)

    def critical(self, msg):
        self.loggerAPI(level="critical", msg=msg)


if __name__ == '__main__':
    LogUtils().debug(msg="哈哈哈哈")
