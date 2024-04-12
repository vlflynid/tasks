from mysql.connector import connect, Error
import logging

from readers import read_file
from writers import write_file

logging.basicConfig(
    filename='app.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class Database:
    def __init__(self, host: str, user: str, password: str, database: str) -> None:
        """
        Initialize the database connection with the given host, user, password, and database.

        Parameters:
            host (str): the host name or IP address of the database server.
            user (str): the username used to authenticate.
            password (str): the password used to authenticate.
            database (str): the name of the database to connect to.

        Returns:
            None
        """
        try:
            self.connection = connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            self.cur = self.connection.cursor(dictionary=True)
        except Error as e:
            logging.error(f"Error connecting to the database: {e}")
            raise e

    def __del__(self):
        self.connection.close()
    
    def insert(self, table: str, data: list) -> None:
        """
        Insert data into the specified table using a list of dictionaries representing rows.

        Parameters:
            table (str): The name of the table to insert data into.
            data (list): A list of dictionaries where each dictionary represents a row to be inserted.

        Returns:
            None
        """
        columns = ', '.join(data[0].keys())
        placeholders = ', '.join(['%s'] * len(data[0]))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        values = [tuple(item.values()) for item in data]
        try:
            self.cur.executemany(query, values)
            self.connection.commit()
            logging.info(f"Successfully inserted {len(data)} rows into {table}")
        except Error as e:
            logging.error(f"Error inserting data into {table}: {e}")

    def get_query_results(self, query_path: str, format) -> None:
        queries = read_file(query_path)
        for key in queries:
            query = queries[key]
            self.cur.execute(query)
            write_file(self.cur.fetchall(), key, format)
    
    
    def prepare_db(self, queries_path: str) -> None:
        """
        A method to prepare the database by executing queries and inserting data.

        Parameters:
            queries (list): A list of SQL queries to be executed.

        Returns:
            None
        """
        queries = read_file(queries_path)
        for query in queries.values():
            self.cur.execute(query)
        self.connection.commit()
    
    