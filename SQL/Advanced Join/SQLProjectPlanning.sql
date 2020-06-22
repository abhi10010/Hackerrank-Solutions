SET 
    sql_mode = '';
SELECT
    Start_Date, End_Date
FROM
    (SELECT 
        Start_Date
     FROM
        Projects
     WHERE
        Start_Date NOT IN (SELECT
                            End_Date
                           FROM
                            Projects)) p1,
    (SELECT 
        End_Date
     FROM
        Projects
     WHERE
        End_Date NOT IN (SELECT
                            Start_Date
                           FROM
                            Projects)) p2
WHERE
    Start_Date < End_Date
GROUP BY
    Start_Date
ORDER BY
    DATEDIFF(End_Date, Start_Date), Start_Date
