import unittest
import mysql.connector
from db.Database import Database, MySqlException

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db_host = "localhost"
        self.db_user = "root"
        self.db_password = "password"
        self.db_name = "test_db"
        self.db = Database(self.db_host, self.db_user, self.db_password, self.db_name)

        # Create a connection to the test database
        self.db.prepare_db()
        self.drop_test_table()
        self.create_test_table()

    def drop_test_table(self):
        query = "DROP TABLE IF EXISTS test_table"
        self.db.cursor.execute(query)
        self.db.connection.commit()

    def insert_test_data(self):
        query = "INSERT INTO test_table (id, name) VALUES (%s, %s)"
        values = [(1, "John"), (2, "Jane")]
        self.db.cursor.executemany(query, values)
        self.db.connection.commit()

    def create_test_table(self):
        query = """
        CREATE TABLE test_table (
            id INT PRIMARY KEY,
            name VARCHAR(50) 
        )
        """
        self.db.cursor.execute(query)
        self.db.connection.commit()

    def test_insert(self):

        table = "test_table"
        data = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]

        self.db.insert(table, data)

        query = "SELECT * FROM test_table"
        self.db.cursor.execute(query)
        result = self.db.cursor.fetchall()

        expected_result =  [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]

        self.assertEqual(result, expected_result)

        self.db.cursor.execute("DeLETE FROM test_table")
    
    def test_insert_no_table(self):
        table = ""
        data = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]

        with self.assertRaises(Exception):
            self.db.insert(table, data)
    
    def test_insert_no_data(self):
        table = "test_table"
        data = []

        with self.assertRaises(Exception):
            self.db.insert(table, data)
    

    def test_get_data(self):
        self.insert_test_data()
        query = "SELECT * FROM test_table"
        result = self.db.get_data(query)

        expected_result =  [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]

        self.assertEqual(result, expected_result)
if __name__ == '__main__':
    unittest.main()