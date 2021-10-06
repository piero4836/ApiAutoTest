
#1.请求域名
from tools.read_yaml import read_yaml

host = "http://127.0.0.1:8083"
login_url = "/userLogin/login"
add_app_url = "/appUpgrade/save"
app_id = None
data_app = read_yaml("mp_app.yaml")
app_type = data_app[0][1]
app_version_name = data_app[0][0]

print(data_app)

#2.请求信息头
headers = {"Content-Type": "application/json", "User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",}