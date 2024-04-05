from mysql.connector import connect, Error
from typing import Union
from getpass import getpass

class DatabaseConnection:
    def __init__(self, host: str, user: str, password: str, database: str) -> None:
        try:
            self.connection = connect(
                host = host,
                user = user,
                password = password,
                database = database
            )
        except Error as e:
            print(e)

    def execute_query(self, query: str, values = None):
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                if values is None:
                    cursor.execute(query)
                else:
                    cursor.executemany(query, values)
                if query.upper().startswith('SELECT'):
                    return cursor.fetchall()
                return None
        except Error as mysql_error:
            print(mysql_error)
        except Exception as e:
            print(e)
    def commit(self):
        self.connection.commit()
        
