from mysql.connector import connect, Error

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
                host = host,
                user = user,
                password = password,
                database = database
            )

            self.cur = self.connection.cursor(dictionary=True)
            self.connection.commit()
        #TODO смарі, якщо є помилка, додати логгер. прінт тебе нічо не вернет. 
        except Error as e:
            print(e)

    def __del__(self):
        self.connection.close()


    def viewAll(self, table: str):
        """
        A function that retrieves all rows from a specified table in the database.

        Parameters:
            table (str): The name of the table from which to retrieve the rows.

        Returns:
            list: A list of tuples representing the rows retrieved from the table.
        """
        self.cur.execute(f"SELECT * FROM {table}")
        result = self.cur.fetchall()
        return result
    
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
        except Error as e:
            print(f"Error inserting data: {e}")

    def getData(self, query: str) -> dict:
        """
        A method to execute a query and retrieve the results.

        Parameters:
            query (str): The SQL query to be executed.

        Returns:
            dict: The results fetched from the database.
        """
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result