USE kream;

create table products (
	id int primary key auto_increment,
	category varchar(45),
	brand varchar(45),
	name varchar(200),
	price varchar(45)
);

INSERT INTO items (category, brand, name, price)
VALUES ("상의","Taejin","태진 콜라보 후드", "1,222,222원");

SELECT * FROM items;

select * from items where name like '%블랙%';
select * from items order by CHAR_LENGTH(price) asc, price asc;

select brand, count(*) from items group by brand;

update items
set name = "태진 콜라보 후드 레드"
where brand = "Taejin";

select * from items where brand = "Taejin";

SELECT i.*, bc.brand_count
FROM items AS i
JOIN (
    SELECT brand, COUNT(*) AS brand_count
    FROM items
    GROUP BY brand
) AS bc
ON i.brand = bc.brand;

-- 안전모드 확인
SELECT @@sql_safe_updates;

-- 안전모드 해제
SET SQL_SAFE_UPDATES = 0;

-- 활성화
SET SQL_SAFE_UPDATES = 1;



