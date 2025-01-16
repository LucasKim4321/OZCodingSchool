SELECT * FROM users;

-- 특정 테이블에서 모든 행 삭제
DELETE FROM users;

-- 특정 조건을 만족하는 행 삭제
DELETE FROM users WHERE age < 18;

-- LIMIT을 사용한 삭제
-- 특정 개수 이상의 행을 삭제하지 않도록 제한
DELETE FROM orders WHERE status = 'canceled' LIMIT 100;

-- `JOIN`을 사용한 삭제
-- 다른 테이블과 조인(join)하여 삭제
DELETE e FROM employees AS e
JOIN departments AS d ON e.department_id = d.id
WHERE d.name = 'Marketing';

-- `USING`을 사용한 삭제
-- 다른 테이블과 조인하여 삭제 (USING 구문 활용)
DELETE FROM employees
USING employees, departments
WHERE employees.department_id = departments.id AND departments.name = 'HR';

-- `RETURNING`을 사용한 삭제 및 반환
-- 삭제한 행 반환 (PostgreSQL에서 사용 가능)
DELETE FROM users WHERE age > 65 RETURNING *;