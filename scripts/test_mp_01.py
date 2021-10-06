import random

import pytest

import api
from api.api_mp import ApiMp
from tools.read_yaml import read_yaml


class TestMp:
    #初始化
    def setup_class(self):
        #获取apiMp对象
        self.mp = ApiMp()
        pass

    @pytest.mark.parametrize("username,password", read_yaml("mp_login.yaml"))
    def test_mp_login(self, username, password):
        self.mp.api_mp_login(username, password)

    def test_app_add(self, versionName=api.app_version_name, type=api.app_type):
        version = "".join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
        self.mp.api_mp_app(version, versionName, type)
