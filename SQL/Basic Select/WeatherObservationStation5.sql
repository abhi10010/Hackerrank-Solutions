SELECT
    CITY, LENGTH(CITY) AS 'LEN'
FROM
    STATION
ORDER BY
    LEN ASC, CITY ASC
LIMIT 1;

SELECT
    CITY, LENGTH(CITY) AS 'LEN'
FROM
    STATION
ORDER BY
    LEN DESC, CITY ASC
LIMIT 1;