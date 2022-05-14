import os

import allure
import pytest

from common.db_utils import db
from common.logger import logger
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


base_data = get_data('base_data.yaml')
login_data = get_data('login_data.yaml')
add_employee_data = get_data('add_employee_data.yaml')
scenario_employee_data = get_data('scenario_employee_data.yaml')
print(scenario_employee_data)

@pytest.fixture(scope="function")
def delete_employee():
    """添加员工前，先删除数据，用例执行之后，再次删除，清理数据"""
    del_sql = base_data["init_sql"]["delete_employee"]
    logger.info(f"前置步骤开始，删除已添加的员工 -> {del_sql}")
    with allure.step(f'前置步骤，清理数据 -> {del_sql}'):
        db.execute_db(del_sql)
    yield
    logger.info(f"后置步骤开始，删除已添加的员工 -> {del_sql}")
    with allure.step(f'后置步骤，清理数据 -> {del_sql}'):
        db.execute_db(del_sql)
