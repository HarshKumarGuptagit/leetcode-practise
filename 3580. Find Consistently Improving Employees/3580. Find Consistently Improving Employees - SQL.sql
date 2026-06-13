{# WITH recent_interview AS(
    SELECT 
        employee_id,
        review_id
    FROM performance_reviews
    WHERE employee_id IN 
    (
        select employee_id
        from performance_reviews
        group by employee_id
        having count(review_id) >=3
    )
    QUALIFY
        ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY review_date DESC) = 1
)

cte AS(
    SELECT 
        employees.employee_id,
        employees.name AS name,
        performance_reviews.review_id,
        performance_reviews.review_date,
        performance_reviews.review_rating AS current_rating,
        LAG(performance_reviews.review_rating,1) OVER (PARTITION BY employees.employee_id ORDER BY performance_reviews.review_date ASC) AS one_prev_rating,
        LAG(performance_reviews.review_rating,2) OVER (PARTITION BY employees.employee_id ORDER BY performance_reviews.review_date ASC) AS two_prev_rating,
    FROM recent_interview
    
    LEFT JOIN 
        employees AS employees
    ON recent_interview.employee_id = employees.employee_id 
    
    LEFT JOIN 
        performance_reviews AS performance_reviews
    ON performance_reviews.employee_id = employees.employee_id
    WHERE recent_interview.review_id IS NOT NULL
)
SELECT 
    employee_id,
    name,
    current_score AS improvement_score,
FROM 
    cte
WHERE 
    current_rating > one_prev_rating
    AND one_prev_rating > two_prev_rating
ORDER BY 
    improvement_score DESC, name ASC
 #}
    ---



-- Optimised one 

WITH cte AS(
    SELECT 
        employee_id,
        rating,
        LAG(rating,1) OVER (PARTITION BY employee_id ORDER BY review_date) AS prev_rating,
        LAG(rating,2) OVER (PARTITION BY employee_id ORDER BY review_date) AS prev2_rating,
        ROW_NUMBER() OVER (PARTITION BY  employee_id ORDER BY review_date desc) AS rn
    FROM 
        performance_reviews
)
SELECT 
    cte.employee_id,
    employees.name,
    cte.prev2_rating - cte.rating AS improvement_score
FROM cte 
LEFT JOIN 
    employees 
ON employees.employee_id = cte.employee_id

WHERE rn = 1
AND prev2_rating IS NOT NULL 
AND prev2_rating< prev_rating AND prev_rating<rating
ORDER BY 
    improvement_score DESC, name ASC