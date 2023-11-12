import pymysql


class DbHelper:

    def __init__(self, host=None, port=None, user=None, password=None, database=None):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)

    def insert_one(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

    def fetch_one(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        result = cur.fetchone()
        self.conn.close()
        return result

    def fetch_all(self, sql):
        """[{"id":1, "name":""}]"""
        cur = self.conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        self.conn.close()
        return result

if __name__ == '__main__':
    db = DbHelper(host="192.168.10.8", port=3306, user="root", password="123456", database="test2")
    sql = "insert into score(`student_id`,`course_id`,`number`) values(2,1,30);"
    db.insert_one(sql)