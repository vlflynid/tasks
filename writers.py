import os
import json
import csv
from dict2xml import dict2xml
def write_data_to_json(data: dict, file_path: str):
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"An error occurred: {e}")

def write_data_to_xml(data: dict, file_path: str):
    try:
        with open(file_path, 'w') as f:
            f.write(dict2xml(data))
    except Exception as e:
        print(f"An error occurred: {e}")

def write_data_to_csv(data: dict, file_path: str):
    try:
        with open(file_path, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            for item in data:
                writer.writerow(item)
    except Exception as e:
        print(f"An error occurred: {e}")

def write_file(data: str, file_name: str, format: str):

    mapping_dict = {
        'json': write_data_to_json,
        'xml': write_data_to_xml,
        'csv': write_data_to_csv
    }

    if not os.path.exists(f"analysed/{format}"):
        os.makedirs(f"analysed/{format}")
    file_path = f"analysed/{format}/{file_name}.{format}"

    return mapping_dict[format](data, file_path)

