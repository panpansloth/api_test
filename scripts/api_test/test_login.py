import allure
import pytest

from api.login_api import login
from common.assert_util import assert_util
from common.logger import logger
from scripts.conftest import login_data


@allure.feature('登录测试模块')
class TestLogin:
    @allure.story("登录测试")
    @pytest.mark.parametrize('login_data', login_data)
    def test_login(self, login_data):
        # 添加动态描述
        allure.dynamic.title(login_data['title'])
        # 调用自己封装的接口
        with allure.step(f"用户登录data -> {login_data['data']}"):
            result = login.login(login_data['data']).json()
        logger.info(f"响应结果result -> {result}")
        logger.info(f"断言 -> 期望结果：{login_data['expected']}，实际结果：{result}")
        with allure.step(f"断言 -> 期望结果：{login_data['expected']}，实际结果：{result}"):
            assert_util(result, login_data['expected'])
