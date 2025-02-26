CREATE DATABASE oz;
USE oz;

CREATE TABLE users (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

SELECT * FROM users;

DROP TABLE users;

select * from boards;

INSERT INTO `oz`.`users` (`id`, `name`, `email`) VALUES ('1', 'test', 'test@test.com');

INSERT INTO `oz`.`boards` (`id`, `title`, `content`, `user_id`) VALUES ('1', '첫번째 게시글', '내용', '1');
