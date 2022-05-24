import requests


# 使用Python装饰器实现单例模式（保证只有一个对象实例的模式），单例类本身的代码不是单例的，通过装饰器使其单例化
def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class Header:
    def __init__(self):
        self.url = 'http://ihrm-test.itheima.net/api/sys/login'
        self.data = {'mobile': '13800000002', 'password': '123456'}

    def get_header(self):
        resp = requests.post(self.url, json=self.data)
        # 从响应体中，获取data值
        token = resp.json().get('data')
        header = {'Content-Type': 'application/json',
                  'Authorization': 'Bearer ' + token}
        return header


# def get_header():
#     url = 'http://ihrm-test.itheima.net/api/sys/login'
#     data = {'mobile': '13800000002', 'password': '123456'}
#     resp = requests.post(url, json=data)
#     # 从响应体中，获取data值
#     token = resp.json().get('data')
#     header = {'Content-Type': 'application/json',
#               'Authorization': 'Bearer ' + token}
#     return header
header = Header()

if __name__ == '__main__':
    header1 = Header()
    header2 = Header()
    print(id(header1), id(header2))
