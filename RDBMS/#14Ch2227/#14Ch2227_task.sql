-- **1. 생성 (CREATE) - 25 문제(필수 : 초급 10문제 / 도전 : 중급 + 고급 15문제)**
USE classicmodels;
SELECT * FROM customers;

-- 초급

-- (1) **`customers`** 테이블에 새 고객을 추가하세요.
INSERT INTO customers (customerNumber, customerName) VALUES (1002, 'Davis');

-- (2) **`products`** 테이블에 새 제품을 추가하세요.
INSERT INTO products (productCode, productName) VALUES ('P001', 'Electronics');

-- (3) **`employees`** 테이블에 새 직원을 추가하세요.
INSERT INTO employees (employeeNumber, lastName, firstName) VALUES (1001, 'Smith', 'John');

-- (4) **`offices`** 테이블에 새 사무실을 추가하세요.
INSERT INTO offices (officeCode, city) VALUES ('1001','New York');

-- (5) **`orders`** 테이블에 새 주문을 추가하세요.
INSERT INTO orders (orderNumber, orderDate) VALUES (3001, '2025-01-05');

-- (6) **`orderdetails`** 테이블에 주문 상세 정보를 추가하세요.
INSERT INTO orderdetails (orderNumber, productCode) VALUES (3001, 'P001');

-- (7) **`payments`** 테이블에 지불 정보를 추가하세요.
INSERT INTO payments (customerNumber, checkNumber, amount) VALUES (1002, '12', 1500.00);
SELECT * FROM payments WHERE customerNumber = 1002;

-- (8) **`productlines`** 테이블에 제품 라인을 추가하세요.
INSERT INTO productlines (productLine, textDescription) VALUES ('Electronics', 'Devices like laptops, smartphones, and tablets.');

-- (9) **`customers`** 테이블에 다른 지역의 고객을 추가하세요.
INSERT INTO customers (customerNumber, customerName,city) VALUES (1003, 'Davis2','New York');

-- (10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
INSERT INTO products (productCode, productName) VALUES ('P002', 'Laptop');
	
-- 중급

-- (1) **`customers`** 테이블에 여러 고객을 한 번에 추가하세요.
INSERT INTO customers (customerNumber, customerName) VALUES
(2001, 'Tech Solutions'),
(2002, 'Green Supplies'),
(2003, 'Alpha Builders');

-- (2) **`products`** 테이블에 여러 제품을 한 번에 추가하세요.
INSERT INTO products (productCode, productName) VALUES
('P003', 'Laptop'),
('P004', 'Smar-- tphone'),
('P005', 'Tablet');

-- (3) **`employees`** 테이블에 여러 직원을 한 번에 추가하세요.
INSERT INTO employees (employeeNumber, lastName, jobTitle) VALUES
(1001, 'Smith', 'Manager'),
(1002, 'Johnson', 'Sales Rep'),
(1003, 'Brown', 'IT Specialist');

-- (4) **`orders`**와 **`orderdetails`**에 연결된 주문을 한 번에 추가하세요.

-- (5)**`payments`** 테이블에 여러 지불 정보를 한 번에 추가하세요.

-- (6) **`customers`** 테이블에 고객을 추가하고 바로 주문을 추가하세요.

-- (7) **`employees`** 테이블에 직원을 추가하고 바로 직급을 할당하세요.

-- (8) **`products`** 테이블에 제품을 추가하고 바로 재고를 업데이트하세요.

-- (9) **`offices`** 테이블에 새 사무실을 추가하고 바로 직원을 할당하세요.

-- (10) **`productlines`** 테이블에 제품 라인을 추가하고 바로 여러 제품을 추가하세요.

-- - 고급

-- (1) **`customers`** 테이블에 새 고객을 추가하고 바로 주문을 추가하세요.

-- (2) **`employees`** 테이블에 새 직원을 추가하고 바로 그들의 매니저를 업데이트하세요.

-- (3) **`products`** 테이블에 새 제품을 추가하고 바로 그 제품에 대한 주문을 추가하세요.

-- (4) **`orders`** 테이블에 새 주문을 추가하고 바로 지불 정보를 추가하세요.

-- (5)**`orderdetails`** 테이블에 주문 상세 정보를 추가하고 바로 관련 제품의 재고를 감소시키세요.

-- - **2. 읽기 (READ) - 25 문제(필수 : 초급 10문제 / 도전 : 중급 + 고급 15문제)**
-- - 초급

-- (1) **`customers`** 테이블에서 모든 고객 정보를 조회하세요.

-- (2) **`products`** 테이블에서 모든 제품 목록을 조회하세요.

-- (3) **`employees`** 테이블에서 모든 직원의 이름과 직급을 조회하세요.

-- (4) **`offices`** 테이블에서 모든 사무실의 위치를 조회하세요.

-- (5) **`orders`** 테이블에서 최근 10개의 주문을 조회하세요.

-- (6) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.

-- (7) **`payments`** 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.

-- (8) **`productlines`** 테이블에서 각 제품 라인의 설명을 조회하세요.

-- (9) **`customers`** 테이블에서 특정 지역의 고객을 조회하세요.

-- (10) **`products`** 테이블에서 특정 가격 범위의 제품을 조회하세요.

-- - 중급

-- (1) **`orders`** 테이블에서 특정 고객의 모든 주문을 조회하세요.

-- (2) **`orderdetails`** 테이블에서 특정 제품에 대한 모든 주문 상세 정보를 조회하세요.

-- (3) **`payments`** 테이블에서 특정 기간 동안의 모든 지불 정보를 조회하세요.

-- (4) **`employees`** 테이블에서 특정 직급의 모든 직원을 조회하세요.

-- (5) **`offices`** 테이블에서 특정 국가의 모든 사무실을 조회하세요.

-- (6) **`productlines`** 테이블에서 특정 제품 라인에 속하는 모든 제품을 조회하세요.

-- (7) **`customers`** 테이블에서 최근에 가입한 5명의 고객을 조회하세요.

-- (8) **`products`** 테이블에서 재고가 부족한 모든 제품을 조회하세요.

-- (9) **`orders`** 테이블에서 지난 달에 이루어진 모든 주문을 조회하세요.

-- (10) **`orderdetails`** 테이블에서 특정 주문에 대한 총 금액을 계산하세요.

-- - 고급

-- (1) **`customers`** 테이블에서 각 지역별 고객 수를 계산하세요.

-- (2) **`products`** 테이블에서 각 제품 카테고리별 평균 가격을 계산하세요.

-- (3) **`employees`** 테이블에서 각 부서별 직원 수를 계산하세요.

-- (4) **`offices`** 테이블에서 각 사무실별 평균 직원 연봉을 계산하세요.

-- (5) **`orderdetails`** 테이블에서 가장 많이 팔린 제품 5개를 조회하세요.

-- - **3. 갱신 (UPDATE) - 25 문제(필수 : 초급 10문제 / 도전 : 중급 + 고급 15문제)**
-- - 초급

-- (1) **`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.

-- (2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.

-- (3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.

-- (4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.

-- (5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.

-- (7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.

-- (8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.

-- (9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.

-- (10) **`products`** 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.

-- - 중급

-- (1) **`employees`** 테이블에서 여러 직원의 부서를 한 번에 갱신하세요.

-- (2) **`offices`** 테이블에서 여러 사무실의 위치를 한 번에 갱신하세요.

-- (3) **`orders`** 테이블에서 지난 달의 모든 주문의 배송 상태를 갱신하세요.

-- (4) **`orderdetails`** 테이블에서 여러 주문 상세의 가격을 한 번에 갱신하세요.

-- (5) **`payments`** 테이블에서 특정 고객의 모든 지불 내역을 갱신하세요.

-- (6) **`productlines`** 테이블에서 여러 제품 라인의 설명을 한 번에 갱신하세요.

-- (7) **`customers`** 테이블에서 특정 지역의 모든 고객의 연락처를 갱신하세요.

-- (8) **`products`** 테이블에서 특정 카테고리의 모든 제품 가격을 갱신하세요.

-- (9) **`employees`** 테이블에서 특정 직원의 모든 정보를 갱신하세요.

-- (10) **`offices`** 테이블에서 특정 사무실의 모든 정보를 갱신하세요.

-- - 고급

-- (1) **`orders`** 테이블에서 지난 해의 모든 주문 상태를 갱신하세요.

-- (2) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 갱신하세요.

-- (3) **`payments`** 테이블에서 지난 달의 모든 지불 내역을 갱신하세요.

-- (4) **`productlines`** 테이블에서 모든 제품 라인의 정보를 갱신하세요.

-- (5) **`customers`** 테이블에서 모든 고객의 주소를 갱신하세요.

-- - **4. 삭제 (DELETE) - 25 문제(필수 : 초급 10문제 / 도전 : 중급 + 고급 15문제)**
-- - 초급

-- (1) **`customers`** 테이블에서 특정 고객을 삭제하세요.

-- (2) **`products`** 테이블에서 특정 제품을 삭제하세요.

-- (3) **`employees`** 테이블에서 특정 직원을 삭제하세요.

-- (4) **`offices`** 테이블에서 특정 사무실을 삭제하세요.

-- (5) **`orders`** 테이블에서 특정 주문을 삭제하세요.

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세를 삭제하세요.

-- (7) **`payments`** 테이블에서 특정 지불 내역을 삭제하세요.

-- (8) **`productlines`** 테이블에서 특정 제품 라인을 삭제하세요.

-- (9) **`customers`** 테이블에서 특정 지역의 모든 고객을 삭제하세요.

-- (10) **`products`** 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.

-- - 중급

-- (1) **`employees`** 테이블에서 특정 부서의 모든 직원을 삭제하세요.

-- (2) **`offices`** 테이블에서 특정 국가의 모든 사무실을 삭제하세요.

-- (3) **`orders`** 테이블에서 지난 달의 모든 주문을 삭제하세요.

-- (4) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 삭제하세요.

-- (5) **`payments`** 테이블에서 특정 고객의 모든 지불 내역을 삭제하세요.

-- (6) **`productlines`** 테이블에서 여러 제품 라인을 한 번에 삭제하세요.

-- (7) **`customers`** 테이블에서 가장 오래된 5명의 고객을 삭제하세요.

-- (8) **`products`** 테이블에서 재고가 없는 모든 제품을 삭제하세요.

-- (9) **`employees`** 테이블에서 특정 직급의 모든 직원을 삭제하세요.

-- (10)**`offices`** 테이블에서 가장 작은 사무실을 삭제하세요.

-- - 고급

-- (1) **`orders`** 테이블에서 지난 해의 모든 주문을 삭제하세요.

-- (2) **`orderdetails`** 테이블에서 가장 적게 팔린 제품의 모든 주문 상세를 삭제하세요.

-- (3) **`payments`** 테이블에서 특정 금액 이하의 모든 지불 내역을 삭제하세요.

-- (4) **`productlines`** 테이블에서 제품이 없는 모든 제품 라인을 삭제하세요.

-- (5) **`customers`** 테이블에서 최근 1년 동안 활동하지 않은 모든 고객을 삭제하세요.