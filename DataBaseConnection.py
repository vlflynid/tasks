from mysql.connector import connect, Error
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

    def execute_query(self, query: str) -> list:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except Error as mysql_error:
            print(mysql_error)
        except Exception as e:
            print(e)

    def execute_update_query(self, query: str) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
        except Error as mysql_error:
            print(mysql_error)
        except Exception as e:
            print(e)


