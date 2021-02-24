# @Author: Chris Paul
# @Time: 2021/02/24 23:06
# @File: Demo1.py.py

import logging
import os
import time
from API_AUTO.utils.pathUtil import pathUtils


logger = logging.getLogger("Demo1")
logger.setLevel(logging.DEBUG)
rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
log_name = pathUtils.pathApi(file_paths=['log','{0}.log'.format(rq)])
pathUtils.create_file(filename=log_name)
with open(file=log_name,encoding="utf-8",mode="a") as file:
    fh = logging.FileHandler(file, mode="w")
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logging.debug("这是一个debug")
    logging.info("这是一个info")
    logging.warning("这是一个warning")
    logging.error("这是一个error")
    logging.critical("这是一个critical")

