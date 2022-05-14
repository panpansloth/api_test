import allure
import pytest

from api.employee_api import employee
from common.assert_util import assert_util
from common.logger import logger
from scripts.conftest import add_employee_data


@allure.feature('添加员工测试模块')
class TestEmpAdd:
    @allure.story('添加员工')
    @allure.description("该用例是针对添加用户接口的测试")
    @pytest.mark.parametrize('add_employee_data', add_employee_data)
    @pytest.mark.usefixtures("delete_employee")
    def test_add_emp(self, add_employee_data):
        # 添加动态描述
        allure.dynamic.title(add_employee_data['title'])
        with allure.step(f"添加员工data -> {add_employee_data['data']}"):
            result = employee.add_employee(add_employee_data['data']).json()
        logger.info(f"响应结果result -> {result}")
        logger.info(f"断言 -> 期望结果：{add_employee_data['expected']}，实际结果：{result}")
        with allure.step(f"断言 -> 期望结果：{add_employee_data['expected']}，实际结果：{result}"):
            assert_util(result, add_employee_data['expected'])
