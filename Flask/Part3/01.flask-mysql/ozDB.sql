CREATE DATABASE oz;
USE oz;

CREATE TABLE users (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE posts(
	id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO posts(title, content) VALUES ("1234","1234");

UPDATE posts SET title='updated09', content='updated09' WHERE id=6;

-- sql인젝션 예시
-- title = "Hacked', 'Malicious Code'); DROP TABLE posts; --"
-- content = "Safe Content"
INSERT INTO posts (title, content) VALUES ('Hacked\', \'Malicious Code\'); DROP TABLE posts; --', 'Safe Content');


SELECT * FROM alembic_version;

SELECT * FROM users;

DROP TABLE users;

select * from boards;

select * from posts;

INSERT INTO `oz`.`users` (`id`, `name`, `email`) VALUES ('1', 'test', 'test@test.com');

INSERT INTO `oz`.`boards` (`id`, `title`, `content`, `user_id`) VALUES ('1', '첫번째 게시글', '내용', '1');
