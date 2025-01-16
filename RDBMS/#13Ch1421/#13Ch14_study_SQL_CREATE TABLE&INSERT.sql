USE testdatabase;

CREATE TABLE users(
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT
);

ALTER TABLE `testdatabase`.`users` 
CHANGE COLUMN `email` `email` VARCHAR(50) NOT NULL ,
ADD UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE;
;

INSERT INTO users(username, email, age) VALUES('inseop', 'inseop@gmail.com', 25);
INSERT INTO users(username, email) VALUES ('inseop2', 'inseop2@gmail.com');

-- VALUES 또는 SET을 사용하여 여러 레코드를 동시에 삽입
INSERT INTO users(username, email) VALUES
('inseop3', 'inseop3@gmail.com'),
('inseop4', 'inseop4@gmail.com'),
('inseop5', 'inseop5@gmail.com');

-- INSERT IGNORE 중복 제한이 있을 때 중복된 값을 추가할 경우 레코드를 추가하지 않고 에러(error)를 방지합니다. 대신 경고(warning)이 발생.
INSERT IGNORE INTO users(username,email,age) VALUES ('john', 'john@gmail.com', 22);
INSERT INTO users(username,email,age) VALUES ('john2', 'john2@gmail.com', 22);

INSERT INTO users(username,email,age) VALUES ('john2', 'john2@gmail.com', 25)
ON DUPLICATE KEY UPDATE username='john2';

-- 중복 에러가 없을 시 INSERT INTO에 명시된 값 추가
-- 중복 에러 발생 시 ON DUPLICATE KEY UPDATE의 내용으로 업데이트
INSERT INTO users(username,email,age) VALUES ('john4', 'john4@gmail.com', 66)
ON DUPLICATE KEY UPDATE username='john5', email = 'john5@gmail.com', age = 33;

-- SET을 사용해 행을 삽입. 여러행 동시 삽입은 안됨!
INSERT INTO users SET username='john6', email='john6@gmail.com', age=66;

-- IGNORE , ON DUPLICATE KEY 둘 다 이렇게 조건시 각각 조건에 맞게 적용됨. 여기선 결국 ON DUPLICATE KEY UPDATE가 됨.
INSERT IGNORE INTO users(username,email,age) VALUES ('john9', 'john9@gmail.com', 99)
ON DUPLICATE KEY UPDATE username='john11', email = 'john11@gmail.com', age = 11;

SELECT * FROM users;

-- 맥 사용시 윈도우랑 다른 단축키를 사용하면서 프로그램내에서 단축키가 이상하게 동작하거나 안되는 등과 같은 상황이 발생할 수도 있다.
-- 예) mysql에서 한글 자판에서 복사키가 안먹힌다... 맥 진심 화가난다... 불편한게 한두가지가 아니다... 하드웨어만 좋음... 하드웨어만 좋다 == 장점이 없다 == 굳이 쓸 이유가 없다
-- 맥은 회사에서 주면 쓰고 절대 사서 쓰지 않겠다!!!