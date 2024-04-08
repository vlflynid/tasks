import DatabaseConnection
import json

class DataManipulation:
    def __init__(self, connection: DatabaseConnection):
        self.connection = connection

    def load_data_from_file(self, file_path, table_name):
        try:
            with open(file_path, 'r') as f:
                json_file = f.read()
                data = json.loads(json_file)
                columns = ', '.join(data[0].keys())
                placeholders = ', '.join(['%s'] * len(data[0]))
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                values = [tuple(item.values()) for item in data]

                self.connection.execute_query(query, values)
                self.connection.commit()

        except FileNotFoundError as e:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in file: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")


    def dump_data_to_file(self, query: str, file_path: str):
        try:
            with open(file_path, 'w') as f:
                json.dump(self.connection.execute_query(query), f, indent=4)
        except Exception as e:
            print(f"An error occurred: {e}")