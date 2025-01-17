USE mysql;
SELECT * FROM user;
USE testdatabase;
USE classicmodels;
SELECT customerName FROM customers;
SELECT customerNumber, customerName FROM customers WHERE customerName LIKE '%taejin%';

SELECT * FROM orders ORDER BY orderDate DESC LIMIT 10;

SELECT * FROM payments WHERE amount >= 100;

SELECT o.orderNumber, c.customerName
FROM orders o
JOIN customers c ON o.customerNumber = c.customernumber;

SELECT p.*, pl.*
FROM products p
JOIN productlines pl ON p.productLine = pl.productLine;

--
SELECT * FROM orderdetails;
SELECT orderNumber, SUM(quantityOrdered * priceEach) AS totalAmount
FROM orderdetails
GROUP BY ordernumber
HAVING totalAmount > 500;
-- HAVING : GROUP BY 로 묶었을 때 WHERE 대신 사용

SELECT customerNumber, SUM(amount) AS totalPayment
FROM payments
GROUP BY customerNumber
HAVING totalPayment > (SELECT AVG(amount) FROM payments);
