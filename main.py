from db.Database import Database
import os
from dotenv import load_dotenv
from readers import read_file
from writers import write_file
from colorama import init, Fore, Style

init(autoreset=True)

load_dotenv()
host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')

queryStudents = read_file('queries/createStudents.sql')
queryRooms = read_file('queries/createRooms.sql')

def create_con():
    con = Database(host, user, password, database)
    return con

def prepare_db(con: Database):
    """
    A function to prepare the database by executing queries and inserting data.
    
    Parameters:
    - con: Database object to interact with the database.
    """
    con.cur.execute(queryStudents)
    con.cur.execute(queryRooms)
    con.insert('rooms', read_file('source/rooms.json'))
    con.insert('students', read_file('source/students.json'))

def ask_query():
    query_num = input(Fore.BLUE + 'Enter query number: ' + Style.RESET_ALL)
    if (os.path.exists(f'queries/Analysis/q{query_num}.sql')):
        return read_file(f'queries/Analysis/q{query_num}.sql')
    else:
        print(Fore.RED + "Query doesn't exist. Try again.")
        ask_query()

def run():
    con = create_con()
    prepare_db(con)
    query = ask_query()
    format = input(Fore.BLUE + 'Enter format: ' + Style.RESET_ALL)
    result = con.getData(query)
    write_file(result, 'result', format)

def main():
    run()

if __name__ == "__main__":
    main()