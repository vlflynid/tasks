SELECT rooms.id, DATEDIFF(now(), MIN(birthday)) - DATEDIFF(now(), MAX(birthday)) AS max_age_diff
FROM rooms JOIN 
	    students ON rooms.id = students.room
GROUP BY rooms.id
HAVING max_age_diff = (
    SELECT MAX(subquery.max_age_diff) 
        FROM (
            SELECT rooms.id, 
                DATEDIFF(now(), MIN(birthday)) - DATEDIFF(now(), MAX(birthday)) AS max_age_diff
            FROM rooms
            JOIN students ON rooms.id = students.room
            GROUP BY rooms.id
        ) AS subquery
    );