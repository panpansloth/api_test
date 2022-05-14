import os
import pprint

from common.logger import logger
from common.read_data import data

import pymysql

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
db_conf = data.load_ini(data_file_path, 'mysql')
db_conf.update(port=int(db_conf['port']))


# print(db_conf)
# print(type(db_conf))


class DBUtil:
    def __init__(self, db_conf=db_conf):
        # 建立数据库连接
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        # 创建游标对象
        self.cursor = self.conn.cursor()

    def __delete__(self):
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()

    def select(self, sql):
        self.conn.ping(reconnect=True)
        self.cursor.execute(sql)
        # 使用fetchall()获取查询结果
        data = self.cursor.fetchall()
        # logger.info(f'sql语句 -> {sql} 查询结果:{data}')
        return data

    def execute_db(self, sql):
        try:
            self.conn.ping(reconnect=True)
            self.cursor.execute(sql)
            self.conn.commit()
            # logger.info(f'sql语句 -> {sql}')
        except Exception as e:
            logger.info(f'操作sql出现错误，错误原因:{e}')
            # 回滚所有更改
            self.conn.rollback()


db = DBUtil(db_conf)
if __name__ == '__main__':
    res = db.select('select * from bs_user;')
    pprint.pprint(res)
    TEL = 13835967925
    delete_sql = f"delete from bs_user where mobile='{TEL}';"
    db.execute_db(delete_sql)

