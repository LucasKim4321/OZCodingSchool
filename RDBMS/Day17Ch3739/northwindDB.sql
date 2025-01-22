-- northwind db

/*
SELECT p.product_name, s.company_name, c.category_name FROM products AS p
JOin suppliers AS s ON p.supplier_id = s.supplier_id 
JOIN categories AS c ON p.category_id = c.category_id;
*/
/*
SELECT category_name, ROUND(AVG(unit_price),2) FROM categories c
JOIN products p ON c.category_id = p.category_id
group by category_name;
*/
/*
SELECT city, company_name, contact_name, 'customers' AS relationship FROM customers
UNION
SELECT city, company_name, contact_name, 'suppliers' AS relationship FROM suppliers;
*/
/*
SELECT YEAR(order_date) as order_year, MONTH(order_date) AS order_month, count(*) AS no_of_orders
FROM orders group by order_year, order_month order by order_year DESC, order_month DESC;
*/
/*
SELECt e.first_name, e.last_name, COUNT(*) AS num_orders,
(
	case
  		WHEN o.shipped_date <= o.required_date THEN 'On Time'
  		WHEN o.shipped_date > o.required_date THEN 'Late'
  		WHEN o.shipped_date IS NULL THEN 'Not Shipped'
  	END
) as shipped
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
group by e.first_name, e.last_name, shipped
order by last_name, first_name, num_orders DESC;
*/

/*
SELECt YEAR(o.order_date) AS order_year, ROUND(SUM(p.unit_price*od.discount*quantity),2) AS discount_amount
FROM order_details od
JOIN orders o ON od.order_id = o.order_id
JOIN products p ON od.product_id = p.product_id
group by order_year
order by order_year DESC;
*/