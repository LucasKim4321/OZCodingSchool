USE testdatabase;

SELECT * FROM users;

UPDATE users
SET username = 'INSEOPS'
WHERE user_id = 1;

-- 아래와 같이 사용시 키 값을 사용해 시도하는게 아니라서 안된다고 에러뜸. (조건을 만족하는 값이 여러개일 수도 있기 때문) 
-- 세이프 모드 해제시 가능
-- SET SQL_SAFE_UPDATES = 0;  -- 0: OFF  1: ON
UPDATE users
SET username = 'SENIOR'
WHERE age = 25;

-- 다른 쿼리문과 함께 실행시 DML(데이터 조작 언어) 쿼리의 영향을 받은 행(row) 수를 반환하는 함수. INSERT,UPDATE,DELETE 등을 감지.
SELECT ROW_COUNT();

-- CASE 문을 사용한 업데이트
-- 세이프 모드 해제시 가능
-- SET SQL_SAFE_UPDATES = 0;  -- 0: OFF  1: ON
UPDATE users
SET username = CASE
	WHEN age >= 60 THEN 'senior'
    ELSE 'young'
END;

-- 이건 세이프 모드랑 관계없음
UPDATE users
SET username = 'TOP5_PEOPLE'
WHERE age >= 50
LIMIT 3;

-- 다른 서브쿼리 결과에 따라 업데이트
UPDATE products
SET price = price * 1.1
WHERE category_id IN (SELECT id FROM categories WHERE name = 'Electronics');

-- 정규 표현식을 활용하여 업데이트
UPDATE users
SET email = CONCAT(email, '_new')
WHERE email REGEXP '@example\.com$';

/*
**REGEXP**는 정규 표현식을 사용하여 email 열의 값이 특정 패턴과 일치하는지 확인합니다.
패턴 설명:
@example\.com$:
@example.com으로 끝나는 문자열을 의미합니다.
.는 정규 표현식에서 "임의의 문자"로 해석되므로, 이를 문자 그대로 매칭하려면 \.로 이스케이프 처리해야 합니다.
$는 문자열 끝을 의미합니다.
SET email = CONCAT(email, '_new'):
››
CONCAT 함수는 문자열을 결합합니다.
기존 email 값에 '_new'를 추가합니다. 예: user@example.com → user@example.com_new.
동작:

email 값이 @example.com으로 끝나는 행만 업데이트됩니다.
해당 조건을 만족하는 email의 끝에 _new가 추가됩니다.
*/


SELECT * FROM users;

