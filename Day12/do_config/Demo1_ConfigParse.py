# author:ChriPaul
# file:Demo1_ConfigParse.py.py
# time:2021/02/12

import configparser

class ConfigParseDemo:
    if __name__ == '__main__':
        configParser = configparser.ConfigParser()
        configParser.read("case.config",encoding="UTF-8")
        mode = configParser.get("MODE","mode")
        print(mode)

