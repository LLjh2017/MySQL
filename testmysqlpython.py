from mysqlpython import Mysqlpython

sql=Mysqlpython("db5")
dele="delete from t1 where name='小孩子'"
sql.zhixing(dele)