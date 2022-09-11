# 插入
import pymysql

"""
数据库操作
"""


def ins(info):
    # 连接database
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="homework_1",
        charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    s = "INSERT INTO `homework_1`.`user_info` (`id`, `dayInfo`) VALUES ('{id}', '{a}');"
    # 执行SQL语句
    for i in range(0, 7):
        cursor.execute(s.format(id=i, a=info[str(i)]))

    conn.commit()

    # 关闭光标对象
    cursor.close()

    # 关闭数据库连接
    conn.close()


def upd(info):
    # 连接database
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="homework_1",
        charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    s = "UPDATE `homework_1`.`user_info` SET `id` = '{id}', `dayInfo` = '{a}' WHERE `id` = '{id}';"
    # 执行SQL语句
    for i in range(0, 7):
        cursor.execute(s.format(id=i, a=info[str(i)]))

    conn.commit()

    # 关闭光标对象
    cursor.close()

    # 关闭数据库连接
    conn.close()


def getOne(id):
    # 连接database
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="homework_1",
        charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    s = "SELECT `id`, `dayInfo` FROM `homework_1`.`user_info` WHERE `id` = '{id}';"
    # 执行SQL语句
    cursor.execute(s.format(id=id))

    res = cursor.fetchone()

    conn.commit()

    # 关闭光标对象
    cursor.close()

    # 关闭数据库连接
    conn.close()

    return res

def getAll():
    # 连接database
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="homework_1",
        charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    s = "SELECT `id`, `dayInfo` FROM `homework_1`.`user_info` WHERE `id` between 0 AND 6"
    # 执行SQL语句
    cursor.execute(s)

    res = cursor.fetchall()

    conn.commit()

    # 关闭光标对象
    cursor.close()

    # 关闭数据库连接
    conn.close()

    return res


def getCnt():
    # 连接database
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="homework_1",
        charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    s = "SELECT `id`, `dayInfo` FROM `homework_1`.`user_info` WHERE `id` = '{id}';"
    # 执行SQL语句
    cursor.execute(s.format(id=7))

    res = cursor.fetchone()

    conn.commit()

    # 关闭光标对象
    cursor.close()

    # 关闭数据库连接
    conn.close()

    return res


def setCnt(cnt):
    res = getCnt()

    # 连接database
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="homework_1",
        charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    if res is None:
        s = "INSERT INTO `homework_1`.`user_info` (`id`, `dayInfo`) VALUES ('7', '{a}');"
        # 执行SQL语句
        cursor.execute(s.format(a = str(cnt)))

        conn.commit()

        # 关闭光标对象
        cursor.close()

        # 关闭数据库连接
        conn.close()
    else:
        s = "UPDATE `homework_1`.`user_info` SET `id` = '7', `dayInfo` = '{a}' WHERE `id` = '7';"
        # 执行SQL语句
        cursor.execute(s.format(a = str(cnt)))

        conn.commit()

        # 关闭光标对象
        cursor.close()

        # 关闭数据库连接
        conn.close()
