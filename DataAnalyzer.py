from DatabaseConnection import DatabaseConnection
from DataManipulation import DataManipulation

class DataAnalyzer:
    def __init__(self, connection: DatabaseConnection):
        self.connection = connection
        self.dumper = DataManipulation(self.connection)

    def get_rooms(self, file_name: str):
        query = """SELECT rooms.id, COUNT(students.id) AS amount FROM
        rooms LEFT JOIN students ON students.room = rooms.id GROUP BY rooms.id"""
        self.dumper.dump_data_to_file(query, file_name)

    def get_yungest_rooms(self, file_name: str):
        query = """SELECT rooms.id
        FROM rooms INNER JOIN students ON students.room = rooms.id
        GROUP BY rooms.id
        ORDER BY AVG(DATEDIFF(now(), birthday))
        LIMIT 5;
        """
        self.dumper = DataManipulation(self.connection)
        self.dumper.dump_data_to_file(query, file_name)

    def get_rooms_with_biggest_age_difference(self, file_name: str):
        query = """SELECT rooms.id, DATEDIFF(now(), MIN(birthday)) - DATEDIFF(now(), MAX(birthday)) AS max_age_diff
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
                    );"""
        self.dumper.dump_data_to_file(query, file_name)

    def get_rooms_with_different_sex(self, file_name: str):
        query = """SELECT rooms.id, 
                          COUNT(CASE WHEN sex='M' THEN 1 ELSE NULL END) AS male_amount, 
                          COUNT(CASE WHEN sex='F' THEN 1 ELSE NULL END) AS female_amount
                   FROM rooms LEFT JOIN students ON students.room = rooms.id
                   GROUP BY rooms.id
                   HAVING male_amount>0 AND female_amount>0;"""
        self.dumper.dump_data_to_file(query, file_name)
    
