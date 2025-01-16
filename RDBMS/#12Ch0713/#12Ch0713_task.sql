```
#### 과제 1: MySQL 사용자 생성 및 권한 부여

목표: MySQL에서 새로운 사용자를 생성하고, 권한을 부여합니다.

##### 개념 설명:

- MySQL 사용자: 데이터베이스에 접근하고 작업을 수행할 수 있는 계정을 의미합니다.
- 권한 부여: 특정 사용자에게 데이터베이스와 테이블에 대해 작업할 수 있는 권한을 부여합니다.
##### 세부 내용:
```
-- 1. MySQL에 root 사용자로 로그인:

- mysql -u root -p 명령어를 사용하여 MySQL에 로그인합니다.
- 이 명령어는 MySQL의 관리자 계정인 root로 로그인하며, 비밀번호를 입력해야 합니다.

-- 2. 새로운 MySQL 사용자 생성:

- CREATE USER 'username'@'localhost' IDENTIFIED BY 'password'; 명령어를 사용하여 새로운 사용자를 생성합니다.
- 예시: 붕어빵 가게의 데이터베이스 관리를 위해 fishbread_user라는 사용자를 생성합니다.
- username에는 새 사용자의 이름, password에는 사용자의 비밀번호를 입력합니다.

-- 3. 사용자에게 권한 부여:

- GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost'; 명령어를 사용하여 새 사용자에게 모든 데이터베이스와 테이블에 대한 모든 권한을 부여합니다.
- 권한을 부여한 후, FLUSH PRIVILEGES; 명령어를 사용하여 변경된 권한을 적용합니다.

-- 4. 부여된 권한 확인:

- SHOW GRANTS FOR 'username'@'localhost'; 명령어를 사용하여 새 사용자에게 부여된 권한을 확인합니다.
- SHOW GRANTS; 명령어를 사용하여 현재 로그인한 사용자의 권한을 확인할 수도 있습니다.

```
#### 과제 2: 데이터베이스와 테이블 생성
목표: 사용자와 주문 정보를 저장할 데이터베이스와 테이블을 생성합니다.

개념 설명:

- 데이터베이스: 데이터를 체계적으로 관리하는 공간입니다.
- 테이블: 데이터베이스 내에서 데이터를 저장하는 구조입니다.

데이터베이스 및 테이블 설계
```

-- 1. 데이터베이스 생성:

- CREATE DATABASE fishbread_db; 명령어를 사용하여 붕어빵 가게의 데이터를 저장할 데이터베이스를 생성합니다.
- USE fishbread_db; 명령어를 사용하여 생성한 데이터베이스를 사용합니다.

-- 2. users 테이블 생성:

- 사용자 정보를 저장하는 테이블을 생성합니다.
- user_id(INT, PRIMARY KEY, AUTO_INCREMENT): 사용자의 고유 ID
- name(VARCHAR(255), NOT NULL): 사용자 이름
- age(INT, NOT NULL): 사용자 나이
- email(VARCHAR(100), UNIQUE): 사용자 이메일
- is_business

-- 3. orders 테이블 생성:

- 주문 정보를 저장하는 테이블을 생성합니다.
- order_id(INT, PRIMARY KEY, AUTO_INCREMENT): 주문의 고유 ID
- user_id(INT, FOREIGN KEY): 주문한 사용자의 ID (users 테이블의 user_id와 참조 관계)
- order_date(DATE): 주문 날짜
- amount(DECIMAL(10, 2)): 주문 금액

-- 4. inventory 테이블 생성:

- 재고 정보를 저장하는 테이블을 생성합니다.
- item_id(INT, PRIMARY KEY, AUTO_INCREMENT): 재고 항목의 고유 ID
- item_name(VARCHAR(255), NOT NULL): 재고 항목 이름
- quantity(INT, NOT NULL): 재고 수량

--  sales 테이블 생성:

- 판매 정보를 저장하는 테이블을 생성합니다.
- sale_id(INT, PRIMARY KEY, AUTO_INCREMENT): 판매의 고유 ID
- order_id(INT, FOREIGN KEY): 주문 ID (orders 테이블의 order_id와 참조 관계)
- item_id(INT, FOREIGN KEY): 재고 항목의 ID (inventory 테이블의 item_id와 참조 관계)
- quantity_sold(INT, NOT NULL): 판매된 수량

-- 6. daily_sales 테이블 생성:

- 일 매출 정보를 저장하는 테이블을 생성합니다.
- date(DATE, PRIMARY KEY): 날짜
- total_sales(DECIMAL(10, 2), NOT NULL): 총 매출
