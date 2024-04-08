import csv
import json
from xml_to_dict import XMLtoDict

def read_csv(file_path):
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            return reader
    except FileNotFoundError as e:
            print(f"File not found: {file_path}")
    except Exception as e:
            print(f"An error occurred: {e}")
    
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.loads(f.read())
            return data
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_xml(file_path):
    try:
        parser = XMLtoDict()
        with open(file_path, 'r') as f:
            data = parser.parse(f.read())
            return data
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
