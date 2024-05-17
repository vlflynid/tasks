from db.Database import Database
from config import *
from readers import read_file
from writers import write_file
import logging

def run():
    """
    Runs the database preparation and analysis processes.

    This function connects to the database, prepares it by creating necessary tables, inserts data into 'rooms' and 'students' tables, reads analysis queries from a file, gets data based on these queries from the database, and writes the results to separate JSON files.

    Parameters:
        None

    Returns:
        None
    """
    try:
        db = Database(HOST, USER, PASSWORD, DATABASE)
        db.prepare_db()
        for table, columns in TABLES.items():
            db.create_table(table, columns)
        db.insert('rooms', read_file(ROOMS))
        db.insert('students', read_file(STUDENTS))
    except Exception as e:
        logging.error(f'Error preparing database: {str(e)}')
    
    try: 
        queries = read_file(ANALYSIS_PATH)
        for name, query in queries.items():
            data = db.get_data(query)
            write_file(data, f'{name}', 'json')
    except Exception as e:
        logging.error(f'Error running analysis: {str(e)}')
        