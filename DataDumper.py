import DatabaseConnection

class DataDumper:
    def __init__(self, connection: DatabaseConnection):
        self.connection = connection

    def dump_data_to_file(self, data, file_path):
        with open(file_path, 'w') as f:
            json.dump(data, f)