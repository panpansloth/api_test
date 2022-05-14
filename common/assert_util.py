# 定义断言通用方法
def assert_util(result, expected):
    assert expected['success'] == result.get('success')
    assert expected['code'] == result.get('code')
    assert expected['message'] in result.get('message')
