# Write your MySQL query statement below
WITH identification_cte AS (
    SELECT 
        s.store_id,
        s.store_name,
        s.location,
        i.product_name,
        i.quantity AS product_quantity,
        i.price AS product_price,
        ROW_NUMBER() OVER (PARTITION BY s.store_id, s.location ORDER BY i.price ASC) AS cheap_flag,
        ROW_NUMBER() OVER (PARTITION BY s.store_id, s.location ORDER BY i.price DESC) AS expensive_flag
    FROM  
        stores AS s
    LEFT JOIN 
        inventory AS i
    ON s.store_id = i.store_id
)
SELECT 
    store_id,
    store_name,
    location,
    MAX(CASE WHEN expensive_flag = 1 THEN product_name END) AS most_exp_product,
    MAX(CASE WHEN cheap_flag = 1 THEN product_name END) AS cheapest_product,
    ROUND(
        MAX(CASE WHEN cheap_flag = 1 THEN product_quantity END)/MAX(CASE WHEN expensive_flag = 1 THEN product_quantity END)
    ,2) AS imbalance_ratio
FROM identification_cte
GROUP BY store_id, store_name, location
HAVING COUNT(product_name) >=3 
AND MAX(CASE WHEN cheap_flag = 1 THEN product_quantity END) > MAX(CASE WHEN expensive_flag = 1 THEN product_quantity END)
ORDER BY imbalance_ratio desc, store_name ASC