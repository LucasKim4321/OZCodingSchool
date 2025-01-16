-- task1

-- root 계정으로 접속
-- 커맨드에 입력 mysql -u root -p 혹은 워크밴치로 접속
CREATE USER 'fishbread_user'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON *.* TO 'fishbread_user'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'fishbread_user'@'localhost';

-- task2


CREATE DATABASE fishbread_db;
USE fishbread_db;

CREATE TABLE users(
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) UNIQUE,
    is_buisness BOOLEAN
);
SELECT * FROM users;

-- DECIMAL(10,2)  소수점 포함 10자리, 소수점은 2자리만

CREATE TABLE orders(
	order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
SELECT * FROM orders;

CREATE TABLE inventory(
	item_id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL
);
SELECT * FROM inventory;

CREATE TABLE sales(
	sale_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    item_id INT,
    quantity_sold INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (item_id) REFERENCES inventory(item_id)    
);
SELECT * FROM sales;

CREATE TABLE daily_sales(
	date DATE PRIMARY KEY,
    total_sales DECIMAL(10,2) NOT NULL
);
SELECT * FROM daily_sales;