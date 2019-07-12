import pymsqlCode


import pymysql

con = pymysql.connect(

    host='127.0.0.1',
    port=3306,
    user='root',
    password='199745',
    charset='utf8',
    db='python'
)

#获取数据库游标（可以得到服务器返回来的结果集，还可以像服务器发送sql语句）
cursor = con.cursor()

pymsqlCode.selFun()

pymsqlCode.batchInsertFun()
