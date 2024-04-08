SELECT rooms.id, 
    COUNT(CASE WHEN sex='M' THEN 1 ELSE NULL END) AS male_amount, 
    COUNT(CASE WHEN sex='F' THEN 1 ELSE NULL END) AS female_amount
FROM rooms LEFT JOIN students ON students.room = rooms.id
GROUP BY rooms.id
HAVING male_amount>0 AND female_amount>0;