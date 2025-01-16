USE testdatabase;

/*
TRUNCATE**는 SQL에서 테이블의 모든 데이터를 빠르게 삭제하는 데 사용되는 명령어입니다. **DELETE**와 비슷한 기능을 하지만, 더 빠르고 효율적이며 몇 가지 차이점이 있습니다.

TRUNCATE TABLE 테이블명;
테이블명: 데이터를 삭제할 테이블의 이름.
실행 시 테이블의 모든 데이터를 삭제하지만, 테이블 구조(스키마)는 유지됩니다.

외례키(Foreign Key)로 엮여있을 경우 안됨.
*/

-- orders 테이블 추가
CREATE TABLE orders (
	order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    product_name VARCHAR(255),
    quantity INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

SELECT * FROM users;
SELECT * FROM orders;

-- 파이썬을 이용해 데이터 랜덤 생성에 사
