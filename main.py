from db.Database import Database
import os
from dotenv import load_dotenv
from readers import read_file
from colorama import init, Fore, Style


init(autoreset=True)

load_dotenv()
host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')


def run():
    con = Database(host, user, password, database)
    con.prepare_db('queries/init.yaml')
    con.insert('rooms', read_file('source/rooms.json'))
    con.insert('students', read_file('source/students.json'))
    con.get_query_results('queries/analysis.yaml', 'csv')


def main():
    run()

if __name__ == "__main__":
    main()