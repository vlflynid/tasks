SELECT rooms.id
FROM rooms INNER JOIN 
    students ON students.room = rooms.id
GROUP BY rooms.id
ORDER BY AVG(DATEDIFF(now(), birthday))
LIMIT 5