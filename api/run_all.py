# 测试单例模式
from api import base_api
from api.employee_api import s1 as ems1
from api.employee_api import s2 as ems2
from api.login_api import s1 as los1
from api.login_api import s2 as los2

print(id(base_api.single1))
print(id(base_api.single2))
print(id(ems1), id(ems2))
print(id(los1), id(los2))
print(base_api.single2.get_common())