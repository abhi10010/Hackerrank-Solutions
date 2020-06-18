SELECT 
    ROUND(S.LAT_N, 4)
FROM
    station S
WHERE
    (SELECT 
        COUNT(Lat_N) 
     FROM 
        station 
     WHERE 
        Lat_N < S.LAT_N ) = (SELECT 
                                COUNT(Lat_N) 
                             FROM 
                                station 
                             WHERE 
                                Lat_N > S.LAT_N)
