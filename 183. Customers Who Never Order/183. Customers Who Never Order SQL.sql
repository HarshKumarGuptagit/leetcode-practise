SELECT 
    name AS Customer
FROM customers
WHERE id NOT IN (
    select distinct customerid from orders
)