#定义函数
import os

import yaml

from config import BASE_PATH


def read_yaml(filename):
    #定义空数组
    arrs = []
    filepath = BASE_PATH + os.sep + "data" + os.sep + filename
    #获取文件流
    with open(filepath, "r", encoding="utf-8") as f:
        # 遍历 调用yaml.safe_load(f).values()方法
        for datas in yaml.safe_load(f).values():
            arrs.append(tuple(datas.values()))
    return arrs

if __name__ == '__main__':
    print(read_yaml("mp_login.yaml"))


