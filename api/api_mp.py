import json

import api
import requests

from tools.get_log import GetLog
from tools.tool import Tool
log = GetLog.get_logger()

class ApiMp:

    #1.初始化
    def __init__(self):

        #1.定义登录接口url
        self.url_login = api.host + api.login_url
        log.info("正在初始化登录 url:{}".format(self.url_login))
        #2.定义添加appurl
        self.url_appurl = api.host + api.add_app_url
        log.info("正在初始化app url:{}".format(self.url_appurl))

    #2.登录接口
    def api_mp_login(self, username, password):
        # 定义请求数据
        data = {"account": username, "password": password, "type": "WEB"}
        log.info("正在执行登录接口,url为:{} 请求数据为:{}".format(self.url_login,data))
        # 调用接口
        json = requests.post(url=self.url_login, json=data, headers=api.headers).json()
        print(json)
        try:
            # 提取sessionId
            Tool.common_session_id(json)
            # 断言
            Tool.common_assert(json)
        except Exception as e:
            log.error("请求出错,错误信息为:{}".format(e))
            raise

    def api_mp_app(self,version, versioName, type):
        # 定义请求数据
        requestData = {"versionName": versioName, "version": version, "type": type}
        # 调用接口
        print(api.headers)
        data = requests.post(url=self.url_appurl, json=requestData, headers=api.headers)
        try:
            print("1111", json.loads(data.text))
            api.app_id = json.loads(data.text).get("data").get("id")
            print("添加app成功,id为:",api.app_id)
            # 断言
            Tool.common_assert(json.loads(data.text))
        except Exception as e:
            log.error("请求出错,错误信息为:{}".format(e))
            raise
