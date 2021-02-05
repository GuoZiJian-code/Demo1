# FileName: Demo1_requests
# Date：2021-02-03 18:15
# Author：CP3

import requests


class requestDemo1:
    def __init__(self, host=None):
        self.host = host

    # get请求
    """
    url = "http://test.cbcs.poly.julytech.cn/developers/view/index.html"
    response = requests.get(url=url, params=None, cookies=None)
    print(response)
    # 响应头 响应状态码 响应报文
    print("响应头:", response.headers)
    print("响应状态码:", response.status_code)
    print("响应报文:", response.text)  # 响应正文格式为html(常用)、xml和Json(常用)
    """

    # 登录，并获取response
    def login(self):
        # post请求 带参数
        url = "{0}/back/authenticate".format(self.host)
        Json_Data = {"username": "admin", "password": "000000", "captcha": "12345", "randomStr": "123456"}
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        return requests.post(url=url, json=Json_Data, headers=headers)

    # 通过登录获取的response获取用户信息
    def getUserInfo(self):
        response = self.login()
        Authorization = response.json()["idToken"]
        headers = {"Content-Type": "application/json;charset=UTF-8", 'Authorization': Authorization,
                   "Cookie": "theme=#409EFF; vue_admin_template_token={0}".format(Authorization)}
        url = "{0}/back/userInfo".format(self.host)
        responseGetUserInfo = requests.get(url=url, headers=headers, cookies=response.cookies)
        print(responseGetUserInfo.json()["userVo"])
        print(responseGetUserInfo.headers)


if __name__ == '__main__':
    rq1 = requestDemo1(url="http://polybzh.julytech.cn")
    rq1.getUserInfo()
