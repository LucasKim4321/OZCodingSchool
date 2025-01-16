-- CREATE DATABASE mydatabase;  -- mydatabase 라는 이름을 가진 데이터베이스를 생성
-- SHOW DATABASES;
-- USE mydatabase;
-- DROP DATABASE IF EXISTS mydatabase;

-- 컨트롤 엔터 혹은 커맨드 엔터시 쿼리문 한줄 실행

-- 1. mysql 유저 확인
USE mysql;
select * from user;

-- 2. mysql 유저 생성
USE mysql;
CREATE USER 'username'@'localhost' IDENTIFIED BY 'user_password';

-- 3. 사용자 비밀번호 변경
SET PASSWORD FOR 'username'@'%' = '신규비밀번호';

-- 4. 권한 부여 (모든 데이터베이스에 대한 권한 부여)
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
FLUSH PRIVILEGES; # 변경된 권한 적용
SHOW GRANTS FOR 'username'@'localhost'; # 부여된 권한 확인
SHOW GRANTS; # 현재 로그인한 유저의 권한 확인

-- 5. 사용자 삭제
USE mysql;
DROP USER 'username'@'%';

