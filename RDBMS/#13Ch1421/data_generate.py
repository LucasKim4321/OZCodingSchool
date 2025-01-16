# 파이썬으로 데터 랜덤 생성하기

# 라이브러리 설치
# python3 --version
# python3 -m pip --version
# python3 -m pip install mysql-connector-python faker
# python3 -m pip show mysql-connector-python faker

import mysql.connector
from faker import Faker
import random #파이썬 기본 모듈

# (1) MYSQL 연결 설정
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='testdatabase'
)

# (2) MYSQL 연결
# cursor를 통해 쿼리 실행
cursor = db_connection.cursor()
faker = Faker()

# users 데이터 생성

for _ in range(100):  # '_'는 반복 변수로, 루프 내부에서 해당 변수를 사용하지 않을 때 관례적으로 사용하는 이름입니다
    username = faker.user_name()
    print (username)
    email = faker.email()

    sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
    values = (username, email)

    # print(sql)
    cursor.execute(sql, values)

# user_id 불러오기
cursor.execute("SELECT user_id FROM users")
valid_user_id = [row[0] for row in cursor.fetchall()]

# orders 100개의 주문 더미 데이터 생성
for _ in range(100):
    user_id = random.choice(valid_user_id)
    product_name = faker.word()
    quantity = random.randint(1,10)

    try:
        sql = "INSERT INTO orders(user_id, product_name, quantity) VALUES(%s, %s, %s)"
        values = (user_id, product_name, quantity)
        cursor.execute(sql, values)
    except:
        print("오류 발생!!")
        pass

db_connection.commit()
cursor.close()
db_connection.close()
