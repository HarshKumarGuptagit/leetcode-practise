# Write your MySQL query statement below
SELECT 
    curr_weather.id
FROM Weather AS curr_weather
LEFT JOIN Weather AS prev_weather
ON curr_weather.recordDate = DATE_add(prev_weather.recordDate,INTERVAL 1 DAY)

WHERE 
    curr_weather.temperature > prev_weather.temperature