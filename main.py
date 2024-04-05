import DatabaseConnection
import DataLoader
import json

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

loader = DataLoader(con)
loader.load_data_from_file('rooms.json', 'rooms')
loader.load_data_from_file('students.json', 'students')

result = con.execute_query('SELECT * FROM students LIMIT 5')
print(json.dumps(result, indent=4))
