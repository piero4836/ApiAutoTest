import random

import pytest
import sys
import os

from locust.user import task, HttpUser
from locust.user.wait_time import between

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from api.api_mp import ApiMp

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://127.0.0.1:8083"

    #初始化
    def setup_class(self):
        #获取apiMp对象
        self.mp = ApiMp()

    def on_start(self):
        self.setup_class()

    #@pytest.mark.parametrize("username,password", read_yaml("mp_login.yaml"))
    @task
    def test_mp_login(self, username="admin", password="123456"):
        self.client.post(url="/userLogin/login", data={"account": username, "password": password, "type": "WEB"})

    # def test_app_add(self, versionName=api.app_version_name, type=api.app_type):
    #     version = "".join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
    #     self.mp.api_mp_app(version, versionName, type)

