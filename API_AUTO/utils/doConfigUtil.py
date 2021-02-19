# FileName: doConfigUtil
# Date：2021-02-19 10:15
# Author：CP3

import configparser


class doConfigUtil:
    @staticmethod
    def readConfig(filename, section, option):
        _configParse = configparser.ConfigParser()
        _configParse.read(filenames=filename, encoding="UTF-8")
        return _configParse.get(section=section, option=option)
