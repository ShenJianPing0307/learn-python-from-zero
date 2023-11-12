import pymysql
from logging import Logger


class DBHelper:

    def __init__(self, host=None, port=None, user=None, password=None, database=None):
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    password=password,
                                    database=database,
                                    cursorclass = pymysql.cursors.DictCursor
                                    )
        self.logger = Logger("SQL")

    def execute(self, sql):
        '''增、删、改  commit'''
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                self.conn.commit()
        except Exception as e:
            self.logger.error("执行SQL错误，错误原因{}，执行SQL:{}".format(e, sql))
            self.conn.rollback()

    def get_all(self, sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            self.logger.error("执行SQL错误，错误原因{}，执行SQL:{}".format(e, sql))

    def get_one(self, sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
                return result
        except Exception as e:
            self.logger.error("执行SQL错误，错误原因{}，执行SQL:{}".format(e, sql))

if __name__ == '__main__':
    db = DBHelper(host="192.168.10.8", port=3306, user="root", password="123456", database="mybatis")
    sql = "SELECT * FROM tb_brand"
    result = db.get_all(sql)
    print(result)