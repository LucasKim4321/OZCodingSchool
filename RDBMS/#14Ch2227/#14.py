import pymysql

connection = pymysql.connect(
    host = '127.0.0.1',
    user='root',
    password='1234',
    # database='classicmodels',  ## DB이름
    db='classicmodels',  ## DB이름
    charset='utf8mb4',  ## 이모지를 위한 설정
    cursorclass = pymysql.cursors.DictCursor
)

connection.curosr()