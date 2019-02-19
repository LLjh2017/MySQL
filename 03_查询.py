import pymysql
db=pymysql.connect(host='localhost',
                   user='root',
                   password='123456',
                   database='db5',
                   charset='utf8')
cursor=db.cursor()
try:
    sel="select * from t1"
    # 得到一堆查询结果,放到cursor游标对象里
    cursor.execute(sel)
    # fetchone取走游标对象里的1条记录
    data1=cursor.fetchone()
    print(data1)
    print("*"*40)
    # 取走游标对象里的多条记录
    data2=cursor.fetchmany(2)
    print(data2)
    print("*"*40)
    # 取走游标对象中剩下的表记录
    data3=cursor.fetchall()
    print(data3)
except Exception as e:
    print('Failed',e)
cursor.close()
db.close()