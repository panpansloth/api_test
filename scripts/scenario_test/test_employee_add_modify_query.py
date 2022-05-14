import allure
import pytest

from api.employee_api import employee
from common.assert_util import assert_util
from common.logger import logger
from scripts.conftest import scenario_employee_data


@allure.epic("针对业务场景的测试")
@allure.feature('场景：添加员工-修改员工-查询员工')
class TestEmpAddModifyQuery:
    @allure.story("用例--添加-修改-查询--预期成功")
    @allure.description("该用例是针对 添加-修改-查询 场景的测试")
    @pytest.mark.parametrize('scenario_employee_data', scenario_employee_data)
    @pytest.mark.usefixtures("delete_employee")
    def test_add_emp(self, scenario_employee_data):
        # 添加动态描述
        allure.dynamic.title(scenario_employee_data['title'])
        # 添加员工
        add_employee_data = scenario_employee_data['add']
        result = employee.add_employee(add_employee_data['data']).json()
        logger.info(f"响应结果result -> {result}")
        assert_util(result, add_employee_data['expected'])
        # 修改员工
        emp_id = result['data']['id']
        modify_employee_data = scenario_employee_data['modify']
        result = employee.modify_employee(emp_id, modify_employee_data['data']).json()
        logger.info(f"响应结果result -> {result}")
        assert_util(result, modify_employee_data['expected'])
        # 查询员工
        query_employee_data = scenario_employee_data['query']
        result = employee.query_employee(emp_id).json()
        logger.info(f"响应结果result -> {result}")
        assert_util(result, query_employee_data['expected'])
