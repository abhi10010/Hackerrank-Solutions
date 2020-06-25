WITH
SDay AS (
    SELECT
        submission_date,
        COUNT(submission_date) AS submissions_per_day
    FROM (
        SELECT DISTINCT
            submission_date,
            hacker_id,
            DENSE_RANK() OVER (PARTITION BY hacker_id ORDER BY submission_date ASC) AS realOrder
        FROM Submissions
    ) T
    WHERE realOrder = DAY(submission_date)
    GROUP BY submission_date
),

STop AS (
    SELECT
        submission_date,
        hacker_id,
        ROW_NUMBER() OVER (
            PARTITION BY submission_date
            ORDER BY submissions_per_hacker DESC, hacker_id ASC
        ) AS ranking
    FROM (
        SELECT
            submission_date,
            hacker_id,
            COUNT(*) AS submissions_per_hacker
        FROM Submissions
        GROUP BY submission_date, hacker_id
    ) T
)
SELECT
    SDay.submission_date,
    SDay.submissions_per_day,
    STop.hacker_id,
    H.name
FROM SDay
LEFT JOIN STop ON SDay.submission_date = STop.submission_date AND STop.ranking = 1
LEFT JOIN Hackers H ON STop.hacker_id = H.hacker_id
ORDER BY SDay.submission_date ASC, STop.hacker_id ASC;
