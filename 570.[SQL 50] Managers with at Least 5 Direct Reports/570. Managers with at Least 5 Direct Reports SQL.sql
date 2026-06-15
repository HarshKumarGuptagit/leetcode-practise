# Write your MySQL query statement below
select name from (
    SELECT 
        m.id,
        m.name
    FROM employee as m
    LEFT JOIN employee AS r
    ON m.id = r.managerId

    GROUP by 1,2
    HAVING COUNT(r.id) >=5
) as t