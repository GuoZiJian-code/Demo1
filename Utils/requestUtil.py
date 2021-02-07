# @Author: Chris Paul
# @Time: 2021/02/04 22:04
# @File: requestUtil.py.py
from json import JSONDecodeError

import requests
from requests import RequestException

from Utils import requestUtil


class RequestUtil:
    def requestMethod(self, url, method, data=None, json=None, cookies=None, headers=None):
        method = method.lower()
        try:
            if method == "get":
                response = requests.get(url=url, data=data, json=json, cookies=cookies, headers=headers)
            elif method == "post":
                response = requests.post(url=url, data=data, json=json, cookies=cookies, headers=headers)
            else:
                response = requests.request(method=method,url=url, data=data, json=json, cookies=cookies, headers=headers)
        except RequestException as e:
            print("请求失败：{0}".format(e))
        except JSONDecodeError as e:
            print("请求失败：{0}".format(e))
        return response


if __name__ == '__main__':
    try:
        url = "http://polybzh.julytech.cn/back/authenticate"
        Json_Data = {"username": "admin", "password": "000000", "captcha": "12345", "randomStr": "123456"}
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        res = RequestUtil().requestMethod(url=url, method="post2222", json=Json_Data, headers=headers)
        print(res.json())
    except JSONDecodeError as e:
        print("Json转换失败，使用text形式:\n{0}".format(res.text))
