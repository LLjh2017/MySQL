import pymysql
# 1.创建数据库连接对象
db=pymysql.connect(host="localhost",
                   user="root",
                   password="123456",
                   database="db5",
                   charset="utf8")
# 2.创建游标对象(利用数据库对象)
cursor=db.cursor()
# 3.执行SQL命令(利用游标对象)
cursor.execute('insert into t1 values(4,"王维",80);')
# 4.提交到数据库执行
db.commit()
print('ok')
# 5.关闭游标对象
cursor.close()
# 6.关闭数据库连接对象
db.close()