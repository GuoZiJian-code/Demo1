# FileName: requestUtil
# Date：2021-02-19 12:00
# Author：CP3


import requests
from API_AUTO.utils.doConfigUtil import doConfigUtil


class requestAPI:
    @staticmethod
    def requestAPI(method, url, option, data=None, json_data=None,
                   headers={"Content-Type": "application/json;charset=UTF-8"}, verify=False):
        if not verify:
            requests.packages.urllib3.disable_warnings()
        url = doConfigUtil.readConfig(filename="E:\PyProject\Demo1\API_AUTO\ConfigFile\TestConfig.conf",
                                      section="url", option=option) + url
        if str(method).upper() == "POST":
            response = requests.post(url=url, data=data, json=json_data, headers=headers, verify=verify)
        elif str(method).upper() == "GET":
            response = requests.get(url=url, data=data, json=json_data, headers=headers, verify=verify)
        else:
            raise ValueError("method传入类型错误，应为GET/POST")
        return response
