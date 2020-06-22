SELECT
    s.Name
FROM
    (Students s
JOIN
    Friends f
    USING(ID)
JOIN
    Packages p
ON
    p.ID = s.ID
JOIN
    Packages p1
ON
    f.Friend_ID = p1.ID)
WHERE
    p.Salary < p1.Salary
ORDER BY
    P1.Salary
