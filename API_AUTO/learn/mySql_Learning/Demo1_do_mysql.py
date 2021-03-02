# @Author: Chris Paul
# @Time: 2021/03/02 21:55
# @File: Demo1_do_mysql.py.py

import MySQLdb

conn = MySQLdb.connect(user="iot",passwd="iot-july-2017",db="jt_lhj",host="rm-wz91spuuq0y4z86kno.mysql.rds.aliyuncs.com")
conn.autocommit(True)
cur = conn.cursor()
sql = "select * from jdt_user where uuid = '{0}'".format("13bca8eaac2ebfaaeffe7fe0f2ab924b")
print(sql)
cur.execute(sql)
results = cur.fetchall()
for item in results:
    print(item)
