SELECT 
    T2.id, T1.age, T1.c, T1.power
FROM
    (SELECT 
        w.id, wp.age, w.coins_needed, w.power 
     FROM 
        Wands w
     INNER JOIN 
        Wands_Property wp 
     ON  
        w.code = wp.code AND 
        wp.is_evil=0) T2
INNER JOIN
    (SELECT 
        wp.age, min(w.coins_needed) c, w.power 
     FROM 
        Wands w 
     INNER JOIN 
        Wands_Property wp 
     ON 
        w.code = wp.code 
     GROUP BY
        wp.age, w.power) T1
WHERE 
    T2.age = T1.age AND 
    T2.power = T1.power AND 
    T2.coins_needed = T1.c 
ORDER BY 
    T1.power DESC, T1.age DESC;
