import requests


def get_header():
    url = 'http://ihrm-test.itheima.net/api/sys/login'
    data = {'mobile': '13800000002', 'password': '123456'}
    resp = requests.post(url, json=data)
    # 从响应体中，获取data值
    token = resp.json().get('data')
    header = {'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + token}
    return header


if __name__ == '__main__':
    header = get_header()
    print(header)
