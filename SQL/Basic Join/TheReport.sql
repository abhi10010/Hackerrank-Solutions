SELECT 
    (CASE  
        WHEN 
            g.Grade >= 8 
        THEN 
            s.Name 
        ELSE 
            NULL 
     END),
     g.Grade,
     s.Marks 
FROM 
    Students s 
INNER JOIN 
    Grades g 
ON 
    s.Marks BETWEEN Min_Mark AND Max_Mark 
ORDER BY 
    g.Grade DESC, s.Name, s.Marks;
