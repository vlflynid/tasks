from db.Database import Database
import os
from dotenv import load_dotenv
from readers import read_csv, read_json
load_dotenv()
host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')


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

              
# con.cur.execute(queryStudents)
# con.cur.execute(queryRooms)

# con.insert('rooms', read_json('json/rooms.json'))
# con.insert('students', read_json('json/students.json'))

#TODO create con, prepare db, read data from file, insert data, execute queries, save results

def create_con():
    con = Database(host, user, password, database)
    return con

def prepare_db(con):
    con.cur.execute(queryStudents)
    con.cur.execute(queryRooms)
    con.insert('rooms', read_json('json/rooms.json'))
    con.insert('students', read_json('json/students.json'))

def run():
    con = create_con()
    prepare_db(con)
    return con

if __name__ == "__main__":
    run()

