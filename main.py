from DatabaseConnection import DatabaseConnection

con = DatabaseConnection('localhost', 'root', 'password', 'task1')

queryStudents = 'CREATE TABLE IF NOT EXISTS students (\
                  birthday DATE, \
                  id INT AUTO_INCREMENT PRIMARY KEY,\
                  name VARCHAR(255),\
                  room INT,\
                  sex VARCHAR(1))'

queryRooms = 'CREATE TABLE IF NOT EXISTS rooms (\
              id INT AUTO_INCREMENT PRIMARY KEY,\
              name VARCHAR(255))'
              
con.execute_query(queryStudents)
con.execute_update_query(queryStudents)


con.execute_query(queryRooms)
con.execute_update_query(queryRooms)

