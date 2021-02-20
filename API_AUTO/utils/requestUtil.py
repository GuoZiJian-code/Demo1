# FileName: requestUtil
# Date：2021-02-19 12:00
# Author：CP3


import requests
from API_AUTO.utils.doConfigUtil import doConfigUtil


class requestAPI:
    @staticmethod
    def requestAPI(method, url, data=None, json_data=None,
                   headers={"Content-Type": "application/json;charset=UTF-8"}, verify=False):
        if not verify:
            requests.packages.urllib3.disable_warnings()
        if str(method).upper() == "POST":
            response = requests.post(url=url, data=data, json=json_data, headers=headers, verify=verify)
        elif str(method).upper() == "GET":
            response = requests.get(url=url, data=data, json=json_data, headers=headers, verify=verify)
        else:
            raise ValueError("method传入类型错误，应为GET/POST")
        return response
