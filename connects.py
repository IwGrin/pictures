import pymysql

def connect():
    '''连接MySQL数据库'''
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='test',
            charset='utf8'
        )
        return conn
    except Exception:
        raise Exception("数据库连接失败")