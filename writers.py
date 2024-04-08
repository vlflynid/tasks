import json

def write_data_to_json(data: dict, file_path: str):
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"An error occurred: {e}")