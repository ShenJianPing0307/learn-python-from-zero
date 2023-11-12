import pymysql

# 1、连接数据库
db = pymysql.connect(host="192.168.10.8", port=3306, user="root", password="123456", database="test2")
# 2、创建游标对象，用来执行sql语句
cursor = db.cursor()
# 3、执行sql语句
cursor.execute("show tables;")
# 4、获取sql执行的结果
result = cursor.fetchall()
print(result)
# 5、关闭连接
db.close()


