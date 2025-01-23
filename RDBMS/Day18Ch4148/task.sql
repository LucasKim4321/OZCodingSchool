-- CREATE DATABASE amazon_test;
USE amazon_test;

-- 회원 테이블
CREATE TABLE Member (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    address VARCHAR(255),
    nickname VARCHAR(100),
    phone_number VARCHAR(20),
    points_balance INT DEFAULT 0
);

-- 카테고리 테이블
CREATE TABLE Category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    genre VARCHAR(100) NOT NULL,
    description TEXT
);

-- 도서 테이블
CREATE TABLE Book (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    publisher VARCHAR(100),
    category_id INT,
    stock INT DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

-- 주문 테이블
CREATE TABLE OrderRecord (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    member_id INT,
    address VARCHAR(255) NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

-- 마일리지 테이블
CREATE TABLE Mileage (
    mileage_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    points_change INT NOT NULL,
    change_date DATE NOT NULL,
    FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

-- 리뷰 테이블
CREATE TABLE Review (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    member_id INT,
    rating TINYINT CHECK (rating BETWEEN 1 AND 5),
    review_date DATE NOT NULL,
    content TEXT,
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

-- 도서-카테고리 관계를 나타내는 중간 테이블 (M:N 관계)
CREATE TABLE BookCategory (
    book_id INT,
    category_id INT,
    PRIMARY KEY (book_id, category_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);
