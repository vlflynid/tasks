SELECT rooms.id, COUNT(students.id) AS amount FROM
    rooms LEFT JOIN students ON students.room = rooms.id GROUP BY rooms.id