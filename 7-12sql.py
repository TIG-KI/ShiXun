import pymysql
import logging

con = pymysql.connect(

    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '199745',
    charset = 'utf8',
    db = 'python'
)

#获取数据库游标（可以得到服务器返回来的结果集，还可以像服务器发送sql语句）
cursor = con.cursor()

def insertFun():
    #向数据库插入一条数据
    #获取数据库游标（可以得到服务器返回来的结果集，还可以像服务器发送sql语句）
    cursor = con.cursor()

    #编写sql语句
    #user name age
    sql = "insert into user values (%d,'%s',%d)"

    #向服务器发送sql语句
    for x in range(2, 13):
        data = (x, "李四", 18)
        sql1 = sql % data
        cursor.execute(sql1)
    #提交
    con.commit()
    con.close()

    print("插入了10条记录")


def selFun():

    #cursor = con.cursor()
    #查询user表中的所有数据并打印出来
    sql = "select * from user"

    cursor.execute(sql)
    #print(cursor.fetchall())

    for x in cursor.fetchall():
        print("id:%d name:%s age:%d" % x)

def batchInsertFun():

    sql1 = "insert into user(name,age) values('李四',18) "
    sql2 = "insert into user(name,age) values('王五',18) "
    sql3 = "insert into user(name,age) values('二哈',18) "
    try:
        #raise TypeError('数据类型错误')
        cursor.execute(sql1)
        cursor.execute(sql2)
        #raise TypeError('数据类型错误')
        cursor.execute(sql3)
    #如果出现错误数据库回滚
    except Exception as e: #所有异常信息都在e指向的对象之中
        con.rollback()
        print(e)
        print("出现问题需要回滚")
    else:
        con.commit()

def closeFun():
    '''
    先关闭游标再关闭连接
    '''
    cursor.close()
    con.close()
    pass

#selFun()
batchInsertFun()

