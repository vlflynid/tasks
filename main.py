from db.Database import Database
import os
from dotenv import load_dotenv
from readers import read_file
from db.DataAnalyzer import get_rooms, get_yungest_rooms, get_rooms_with_biggest_age_difference, get_rooms_with_different_sex


load_dotenv()
host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')


#TODO усе квері храні в отдельном файліке .json .yml .sql .py 
#ОНО?

queryStudents = read_file('queries/createStudents.sql', 'sql')
queryRooms = read_file('queries/createRooms.sql', 'sql')
#TODO create con, prepare db, read data from file, insert data, execute queries, save results

def create_con():
    con = Database(host, user, password, database)
    return con

def prepare_db(con: Database):
    con.cur.execute(queryStudents)
    con.cur.execute(queryRooms)
    con.insert('rooms', read_file('json/rooms.json', 'json'))
    con.insert('students', read_file('json/students.json', 'json'))

def analyse_data(con: Database):
    get_rooms(con, 'analysed/q1_result.json')
    get_yungest_rooms(con, 'analysed/q2_result.json')
    get_rooms_with_biggest_age_difference(con, 'analysed/q3_result.json')
    get_rooms_with_different_sex(con, 'analysed/q4_result.json')
    pass

def run():
    con = create_con()
    prepare_db(con)
    analyse_data(con)
    return con

if __name__ == "__main__":
    run()

