USE yes24;

CREATE TABLE Books (
	bookID INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    publisher VARCHAR(255),
    publishing DATE,
    rating DECIMAL(3,1),
    review INT,
    sales INT,
    price DECIMAL(10,2),
    ranking INT,
    ranking_weeks INT
);

SELECT * FROM Books;
DROP TABLE Books;

SELECT * FROM books WHERE rating >= 8;
SELECT title, review FROM books where REVIEW >= 100 ORDER BY review DESC;
SELECT title, price FROM books WHERE price >= 20000;
SELECT author, COUNT(*) AS books_count FROM books GROUP BY author ORDER BY books_count DESC;
SELECT publisher, COUNT(*) AS publishing_count FROM books GROUP BY publisher;
SELECT author, AVG(rating) AS rating_avg FROM books GROUP BY author ORDER BY rating_avg;
SELECT * FROM books WHERE ranking = 1;

-- 집계 및 그룹화
SELECT sales, review, title FROM books ORDER BY sales DESC, review DESC LIMIT 10;
SELECT * FROM books ORDER BY publishing DESC;
SELECT author, AVG(rating) AS rating_avg FROM books GROUP BY author ORDER BY rating_avg DESC;
SELECT publishing, COUNT(*) FROM books GROUP BY publishing;
SELECT author, AVG(price) AS price_avg FROM books GROUP BY author ORDER BY price_avg DESC;
SELECT * FROM books ORDER BY review DESC LIMIT 5;
SELECT ranking, AVG(review) FROM books GROUP BY ranking;


-- -------------------
--  서브쿼리 및 고급 기능
-- -------------------

-- 평균 평점보다 높은 평점을 받은 책들을 조회하세요.
SELECT title, rating FROM books WHERE rating > (SELECT AVG(rating) FROM books) ORDER BY rating DESC;
-- 평균 가격보다 비싼 책들의 제목과 가격을 조회하세요.
SELECT title, price FROM books WHERE price > (SELECT AVG(price) FROM books) ORDER BY price DESC;
-- 가장 많은 리뷰를 받은 책보다 많은 리뷰를 받은 다른 책들을 조회하세요.
SELECT title, review FROM books WHERE review > (SELECT MAX(review) FROM books) ORDER BY review DESC;
-- 평균 판매지수보다 낮은 판매지수를 가진 책들을 조회하세요.
SELECT title, sales FROM books WHERE sales < (SELECT AVG(sales) FROM books);
-- 가장 많이 출판된 저자의 책들 중 최근에 출판된 책을 조회한세요.
SELECT author,COUNT(*) FROM books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1;
SELECT title, author, publishing FROM books WHERE author = (SELECT author FROM books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1) ORDER BY publishing DESC;


-- -------------------
--  데이터 수정 및 관리
-- -------------------
select * from books; 
UPDATE Books SET price = 99999 WHERE title = '소년이 온다';
UPDATE Books SET price = 99999 WHERE bookId = 1;
CREATE TEMPORARY TABLE temp_min AS SELECT MIN(sales) FROM books;
DELETE FROM books WHERE sales = (SELECT MIN(sales) FROM books);
UPDATE books SET rating = rating + 1 WHERE publisher = '창비';
-- 저자별 평균 평점 및 판매지수를 분석하여 인기 있는 저자를 확인합니다.
SELECT author, AVG(rating), AVG(sales) FROM books GROUP BY author ORDER BY AVG(rating) DESC, AVG(sales) DESC;
-- 출판일에 따른 책 가격의 변동 추세를 분석합니다.
SELECT publishing, AVG(price) FROM books GROUP BY publishing;
-- 출판사별 출간된 책의 수와 평균 리뷰 수를 비교 분석합니다.
SELECT publisher, count(*) AS count_books, AVG(review) FROM books GROUP BY publisher ORDER BY count_books DESC;
-- 국내도서랭킹과 판매지수의 상관관계를 분석합니다. 양의 상관관게 하나가 오르면 다른하나도 오른다. 음의 상관관계 하나가 오르면 다른하나는 감소한다.
SELECT ranking, AVG(sales) FROM books GROUP BY ranking;
-- 가격 대비 리뷰 수와 평점의 관계를 분석하여 가성비 좋은 책을 찾습니다.
SELECT price, AVG(review), AVG(rating) FROM books GROUP BY price;


-- -------------------
--  난이도 있는 문제
-- -------------------
USE yes24;
SELECT * FROM books;

-- 출판사별 평균 판매지수가 가장 높은 저자 찾기
-- 각 출판사별로 평균 판매지수가 가장 높은 저자의 이름과 그 평균 판매지수를 조회하세요.
SELECT publisher, author, AVG(sales) AS avg_sales FROM books
GROUP BY publisher, author ORDER BY publisher, avg_sales DESC;
    
-- 리뷰 수가 평균보다 높으면서 가격이 평균보다 낮은 책 조회
-- 리뷰 수와 가격의 전체 평균을 계산한 후, 이보다 리뷰 수는 높고 가격은 낮은 책들을 조회하세요.

SELECT title, review, price FROM books WHERE review > (SELECT AVG(review) FROM books) AND price < (SELECT AVG(price) FROM books);
    
-- 가장 많은 종류의 책을 출판한 저자 찾기
-- 서로 다른 제목의 책을 가장 많이 출판한 저자를 찾으세요.  -- DISTINCT title 중복없는 제목
SELECT author, count(DISTINCT title) AS num_books FROM books GROUP BY author ORDER BY num_books DESC LIMIT 1;

-- 각 저자별로 가장 높은 판매지수를 기록한 책 조회
-- 각 저자별로 가장 높은 판매지수를 기록한 책의 제목과 그 판매지수를 조회하세요.

SELECT author, MAX(sales) AS max_sales FROM books GROUP BY author;

-- 연도별 출판된 책 수와 평균 가격 비교
-- 연도별로 출판된 책의 수와 그 해 출판된 책들의 평균 가격을 비교 분석하세요.

SELECT YEAR(publishing) AS year, COUNT(*) AS num_books, AVG(price) AS avg_price FROM books GROUP BY year;
SELECT MONTH(publishing) AS month, COUNT(*) AS num_books, AVG(price) AS avg_price FROM books GROUP BY month;
    
SELECT * FROM books;
-- 출판사가 같은 책들 중 평점 편차가 가장 큰 출판사 찾기
-- 같은 출판사에서 출판된 책들 중 평점 편차가 가장 큰 출판사와 그 편차를 조회하세요.

    SELECT publisher, MAX(rating) - MIN(rating) as rating_difference
    FROM Books
    GROUP BY publisher
    ORDER BY rating_difference DESC;
    
    SELECT publisher, MAX(rating) - MIN(rating) as rating_difference
    FROM Books
    GROUP BY publisher
    HAVING COUNT(*) >= 2
    ORDER BY rating_difference DESC;
    
-- 특정 저자의 책들 중 판매지수 대비 평점이 가장 높은 책 찾기
-- 특정 저자의 책들 중 판매지수 대비 평점이 가장 높은 책의 제목과 그 비율을 조회하세요.
    
    SELECT title, rating / sales as ratio
    FROM Books
    WHERE author = '특정 저자'
    ORDER BY ratio DESC
    LIMIT 1;

