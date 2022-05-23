import os

# from api import base_api
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path, 'host')['api_root_url']

# s1 = base_api.single1
# s2 = base_api.single2


class LoginApi(RestClient):
    def __init__(self, api_root_url):
        super().__init__(api_root_url)
        # print(id(s1))
        # print(id(s2))

    # 登录
    def login(self, data):
        return self.post('/sys/login', json=data)


login = LoginApi(api_root_url)
if __name__ == '__main__':
    data = {"mobile": "13800000002", "password": "123456"}
    resp = login.login(data)
    print(resp.json())
