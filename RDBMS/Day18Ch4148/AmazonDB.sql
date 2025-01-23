-- 서버에 타이머가 설정되어있어서 오래걸릴시 타임아웃되서 에러남.
SELECT * FROM book WHERE title='abc';

SELECT * FROM book;
SELECT * FROM book WHERE title='Database-SQL-Rdbms Howto';
SELECT title FROM book WHERE title LIKE 'd%o';
SELECT d.* FROM (SELECT title FROM book WHERE title LIKE 'd%') AS d
WHERE d.title='Database-SQL-Rdbms Howto';

-- “이름 정렬한 후” 절반씩 나눠서 찾는 값이 중간값보다 작은가 큰가 반복  (이진탐색)

-- 인덱스로 책을 분류해놓은 상태에서 찾음
-- 특정한 분류법에 따라 모든책에 인덱스로 구분 후 이진탐색함

-- title을 인덱스 구조로 변환
ALTER TABLE book ADD INDEX idx_title (title);

-- 인덱스 확인
SHOW INDEX FROM book;  -- title에 인덱스 적용 시 idx_title가 생겨 있음

