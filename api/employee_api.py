import os
from common.get_header import get_header
from common.read_data import data
from core.rest_client import RestClient
# from api import base_api

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path, 'host')['api_root_url']
header = get_header()

# s1 = base_api.single1
# s2 = base_api.single2


class EmployeeApi(RestClient):
    def __init__(self, api_root_url):
        super().__init__(api_root_url)
        # print(id(s1))
        # print(id(s2))

    # 添加员工
    def add_employee(self, data):
        return self.post('/sys/user', json=data, headers=header)

    # 查询员工
    def query_employee(self, emp_id):
        url = '/sys/user/' + emp_id
        return self.get(url, headers=header)

    # 修改员工
    def modify_employee(self, emp_id, modify_data):
        url = '/sys/user/' + emp_id
        return self.put(url, headers=header, json=modify_data)

    # 删除员工
    def delete_employee(self, emp_id):
        url = '/sys/user/' + emp_id
        return self.delete(url, headers=header)


employee = EmployeeApi(api_root_url)
if __name__ == '__main__':
    # header = {'Content-Type': 'application/json',
    #           'Authorization': 'Bearer 829d3b0e-08ca-4d89-942c-9389e2a81ed0'}
    # data_add = {
    #     'username': '业务猪001',
    #     'mobile': '13678428776',
    #     'workNumber': '7527'
    # }
    # resp = employee.add_employee(data_add)
    # print('添加: ', resp.json())

    employee_id = '1520781377375682560'
    # resp = employee.query_employee(emp_id=employee_id)
    # print('查询: ', resp.json())

    # data = {'username': '齐天大圣'}
    # resp = employee.modify_employee(employee_id, data)
    # print('修改: ', resp.json())
    #
    resp = employee.delete_employee(employee_id)
    print('删除: ', resp.json())
