USE airbnb;

-- VARCHAR UTF-8 문자셋 사용 시, 한 글자가 최대 4바이트이므로, 최대 약 1KB(255 × 4)
-- decimal(자리값,소수점 자리) 소수점 이하 자리까지 포함해 자리값 만큼의 최대 자리수를 가짐.
-- TIMESTAMP 

-- Products 테이블
CREATE TABLE Products (
	productID INT AUTO_INCREMENT PRIMARY KEY,
    productName VARCHAR(255) NOT NULL,
    price decimal(10,2) NOT NULL,
    stockQuantity INT NOT NULL,
    createDate TIMESTAMP
);

-- Customers 테이블
CREATE TABLE Customers (
	customerID INT AUTO_INCREMENT PRIMARY KEY,
    customerName VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    address TEXT NOT NULL,
    createDate TIMESTAMP
);

-- Orders 테이블
CREATE TABLE Orders (
	orderID INT AUTO_INCREMENT PRIMARY KEY,
    customerID INT,
    orderDate TIMESTAMP,
    totalAmount DECIMAL(10,2),
    FOREIGN KEY (customerID) REFERENCES Customers(customerID)
);

SELECT * FROM orders;
SELECT * FROM Customers;
SELECT * FROM Products;