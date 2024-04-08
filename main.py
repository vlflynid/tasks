from DatabaseConnection import DatabaseConnection
from DataManipulation import DataManipulation
from DataAnalyzer import DataAnalyzer


con = DatabaseConnection('localhost', 'root', 'password', 'task1')

queryStudents = 'CREATE TABLE IF NOT EXISTS students (\
                  birthday VARCHAR(255), \
                  id INT PRIMARY KEY,\
                  name VARCHAR(255),\
                  room INT,\
                  sex VARCHAR(1))'

queryRooms = 'CREATE TABLE IF NOT EXISTS rooms (\
              id INT PRIMARY KEY,\
              name VARCHAR(255))'

              
con.execute_query(queryStudents)

con.execute_query(queryRooms)

data = DataManipulation(con)
data.load_data_from_file('rooms.json', 'rooms')
data.load_data_from_file('students.json', 'students')

analysis = DataAnalyzer(con)
analysis.get_rooms('rooms_q1.json')

analysis.get_yungest_rooms('yungest_rooms.json')
analysis.get_rooms_with_different_sex('sex_rooms.json')
analysis.get_rooms_with_biggest_age_difference('age_diff_rooms.json')