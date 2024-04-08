from mysql.connector import connect, Error

class Database:
    def __init__(self, host: str, user: str, password: str, database: str) -> None:
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
        self.cur.execute(f"SELECT * FROM {table}")
        result = self.cur.fetchall()
        return result
    
    def insert(self, table: str, data: dict) -> None:
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
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result