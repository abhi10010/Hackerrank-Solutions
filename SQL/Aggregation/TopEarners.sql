SELECT
    (salary * months) as earnings, 
    COUNT(*)
FROM
    Employee
GROUP BY 
    1
ORDER BY
    1 DESC
LIMIT 1;
