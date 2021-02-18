# author:ChriPaul
# file:doConfigUtil.py
# time:2021/02/13

import configparser


class doConfigUtil:
    @classmethod
    def readConfig(cls, filenames, section, option):
        configParser = configparser.ConfigParser()
        configParser.read(filenames=filenames, encoding="UTF-8")
        return configParser.get(section=section, option=option)

