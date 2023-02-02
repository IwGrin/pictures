from connects import connect

def qureyOne(sql):
    '''执行sql语句,返回一行'''
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        return res[0][0]
    except Exception:
        print("Error:unable to fetch data")
    cursor.close()
    conn.close()

def qureyMuti(sql):
    '''执行sql语句，返回多行'''
    try:
        resArr = []
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            resArr.append(row)
        return resArr
    except Exception:
        print("Error:unable to fetch data")
    cursor.close()
    conn.close()