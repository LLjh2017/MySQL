import pymysql
db=pymysql.connect(host='localhost',
                   user='root',
                   password='123456',
                   database='db5',
                   charset='utf8')
cursor=db.cursor()
# 增加
ins='insert into t1(name,score) values("小姐姐",88)'
cursor.execute(ins)
# 修改
upd='update t1 set score=100 where name="李白"'
cursor.execute(upd)
# 删除
dele='delete from t1 where name="王维"'
cursor.execute(dele)
db.commit()
cursor.close()
db.close()