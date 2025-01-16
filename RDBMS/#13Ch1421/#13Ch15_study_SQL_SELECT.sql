USE testdatabase;

SELECT user_id, username FROM users;
SELECT age, age *100 FROM users;
SELECT age, age *100 as age100 FROM users;
SELECT * FROM users ORDER BY age;  -- 기본값 ASC
SELECT * FROM users ORDER BY age DESC;
SELECT * FROM users ORDER BY age ASC;
SELECT * FROM users WHERE age >= 25;
SELECT * FROM users WHERE username = 'inseop' AND age >= 25;
SELECT * FROM users WHERE NOT age >= 25;
SELECT * FROM users WHERE age BETWEEN 25 AND 50;
SELECT * FROM users WHERE age BETWEEN 25 AND 50 LIMIT 2;
SELECT * FROM users LIMIT 7, 3;  -- 8 부터 3개
SELECT * FROM users LIMIT 3 OFFSET 7;  -- 8 부터 3개
SELECT age, COUNT(*) AS age_count FROM users GROUP BY age;

SELECT username, age,
CASE
	WHEN age >= 30 THEN '성인'
    WHEN age <= 14 THEN '초딩'
    ELSE '미성년자'
END AS age_group FROM users;

SELECT
	username, age,
    ROW_NUMBER() OVER (ORDER BY age DESC) AS 'rank'
FROM users;

SELECT
	username, age,
    ROW_NUMBER() OVER (ORDER BY age DESC) AS age_rank
FROM users;