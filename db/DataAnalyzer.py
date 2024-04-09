from db.Database import Database
from readers import read_sql
from writers import write_file


def get_rooms(con: Database, file_name:str, format: str):
    query = read_sql('queries/Analysis/q1.sql') 
    data = con.getData(query)
    write_file(data, file_name, format)


def get_yungest_rooms(con: Database, file_name: str, format: str):
    query = read_sql('queries/Analysis/q2.sql')
    data = con.getData(query)
    write_file(data, file_name, format)

def get_rooms_with_biggest_age_difference(con: Database, file_name: str, format: str):
    query = read_sql('queries/Analysis/q3.sql')
    data = con.getData(query)
    write_file(data, file_name, format)

def get_rooms_with_different_sex(con: Database, file_name: str, format: str):
    query = read_sql('queries/Analysis/q4.sql')
    data = con.getData(query)
    write_file(data, file_name, format)