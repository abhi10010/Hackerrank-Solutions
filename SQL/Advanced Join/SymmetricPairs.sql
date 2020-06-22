SELECT
    CASE 
        WHEN X > Y 
        THEN Y 
        ELSE X
    END AS Small,
    CASE
        WHEN X > Y 
        THEN X
        ELSE Y
    END AS Big
FROM
    Functions
GROUP BY
    Small, Big
HAVING
    COUNT(*) > 1
