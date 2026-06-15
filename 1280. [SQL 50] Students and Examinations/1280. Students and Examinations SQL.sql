# Write your MySQL query statement below
SELECT 
    students.student_id,
    students.student_name,
    subjects.subject_name,
    COUNT(examinations.subject_name) AS attended_exams
FROM 
    students
CROSS JOIN 
    subjects
LEFT JOIN   
    Examinations
ON examinations.student_id = students.student_id
AND examinations.subject_name = subjects.subject_name

GROUP BY 1,2,3
ORDER BY 1 ASC, 2 ASC