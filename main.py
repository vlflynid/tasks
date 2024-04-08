from DatabaseConnection import DatabaseConnection
from DataManipulation import DataManipulation
from DataAnalyzer import DataAnalyzer
import os
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')


#TODO add .env - load variables from dotenv. read about pydantic settings
con = DatabaseConnection(host, user, password, database)

#TODO усе квері храні в отдельном файліке .json .yml .sql .py 
queryStudents = """CREATE TABLE IF NOT EXISTS students (
                  birthday VARCHAR(255), 
                  id INT PRIMARY KEY,
                  name VARCHAR(255),
                  room INT,
                  sex VARCHAR(1))"""

queryRooms = """CREATE TABLE IF NOT EXISTS rooms (
              id INT PRIMARY KEY,
              name VARCHAR(255))"""

              
con.execute_query(queryStudents)
con.execute_query(queryRooms)

data = DataManipulation(con)
data.load_data_from_file('rooms.json', 'rooms')
data.load_data_from_file('students.json', 'students')

analysis = DataAnalyzer(con)
analysis.get_rooms('rooms_q1.json')

analysis.get_yungest_rooms('yungest_rooms.json')
analysis.get_rooms_with_different_sex('sex_diff_rooms.json')
analysis.get_rooms_with_biggest_age_difference('age_diff_rooms.json')

# create con, prepare db, read data from file, insert data, execute queries, save results

# def create_con():
#     pass

# def prepare_db():
#     pass

# def run():
#     create_con()
#     prepare_db()
#     pass

# if __name__ == "__main__":
#     run()