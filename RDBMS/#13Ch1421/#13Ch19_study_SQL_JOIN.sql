
SELECT * FROM users;
SELECT * FROM orders;

SELECT * FROM users
INNER JOIN orders ON users.user_id = orders.user_id;

SELECT * FROM users
LEFT JOIN orders ON users.user_id = orders.user_id;