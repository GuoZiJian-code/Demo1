# @Author: Chris Paul
# @Time: 2021/02/04 22:04
# @File: requestUtil.py.py

import requests
from Utils import requestUtil


class RequestUtil:
    def requestMethod(self, url, method, data=None, json=None, cookies=None, headers=None):
        method = method.lower()
        if method == "get":
            response = requests.get(url=url, data=data, json=json, cookies=cookies, headers=headers)
        elif method == "post":
            response = requests.post(url=url, data=data, json=json, cookies=cookies, headers=headers)
        else:
            pass
        return response


if __name__ == '__main__':
    url = "http://polybzh.julytech.cn/back/authenticate"
    Json_Data = {"username": "admin", "password": "000000", "captcha": "12345", "randomStr": "123456"}
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    res = RequestUtil().requestMethod(url=url, method="post", json=Json_Data, headers=headers)
    print(res.json())
