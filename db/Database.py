import mysql.connector
from mysql.connector import Error, errors  
import logging
from config import LOGFILE
class MySqlException(Exception):
    pass
class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        
        logging.basicConfig (
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    def close(self):
        self.connection.close()
        self.cursor.close()

    def connect(self):
        """
        Attempt to establish a connection to the database using the specified host, user, and password.
        
        Parameters:
            self (Database): The current instance of the Database class.
            
        Returns:
            None
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
            )
            self.cursor = self.connection.cursor(dictionary= True)
            logging.info('Connected to the database')
        except errors.DatabaseError as e:
            logging.error(f'Error connecting to database: {str(e)}')

    def prepare_db(self):
        """
        Prepares the database by connecting, creating the schema, and selecting the schema.

        Parameters:
            self (Database): The current instance of the Database class.

        Raises:
            Exception: If an error occurs during the preparation process.

        Returns:
            None
        """
        try:
            self.connect()
            self.create_schema()
            self.select_schema(self.database)
        except Exception as e:
            logging.error(f'Error preparing database: {str(e)} - {e.args}')

    def create_table(self, table_name, columns):
        try:
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
            self.cursor.execute(query)
            self.connection.commit()
        except Error as e:
            raise Exception(f'Error creating table: {table_name}, {str(e)}')
    
    def create_schema(self):
        """
        Creates a schema in the MySQL database.

        This function executes a SQL query to create a database schema if it does not already exist. The name of the schema is determined by the value of the `self.database` attribute.

        Parameters:
            self (Database): The current instance of the Database class.

        Raises:
            MySqlException: If there is an error creating the schema. The exception message will include the specific error message.

        Returns:
            None
        """
        try:
            query = "CREATE DATABASE IF NOT EXISTS %s" % self.database
            self.cursor.execute(query)
            self.connection.commit()
            logging.info('Schema created successfully')
        except Error as e:
            raise Exception(f'Error creating schema: {str(e)}')

    def select_schema(self, schema_name):
        """
        Selects a schema in the MySQL database.

        Args:
            schema_name (str): The name of the schema to select.

        Raises:
            MySqlException: If there is an error selecting the schema.

        Returns:
            None
        """
        try:
            query = "USE %s" % schema_name
            self.cursor.execute(query)
            logging.info('Schema selected successfully')
        except Error as e:
            raise Exception(f'Error selecting schema: {str(e)}')
        
    def get_data(self, query: str):
        """
        Executes the given SQL query and returns the result as a list of dictionaries.

        Parameters:
            query (str): The SQL query to execute.

        Returns:
            list: A list of dictionaries representing the result of the query. Each dictionary represents a row in the result set, with the keys being the column names and the values being the corresponding values in each row.

        Raises:
            Error: If an error occurs while executing the query. The error message and arguments are logged.
        """
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            logging.error(f"Error executing query: {str(e)} - {e.args}")


    
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
            self.cursor.executemany(query, values)
            self.connection.commit()
            logging.info(f"Successfully inserted {len(data)} rows into {table}")
        except Error as e:
            raise Exception(f"Error inserting data into {table}: {str(e)}")

    
    