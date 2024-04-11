import os
import csv
import json
from xml_to_dict import XMLtoDict

def read_csv(file_path) -> list:
    """
    Read a CSV file and return its contents as a list.

    :param file_path: The path to the CSV file to be read.
    :return: A list containing the data from the CSV file.
    """
    try:
        with open(file_path, 'r') as f:
            data = list(csv.DictReader(f, delimiter=","))
            return data
    except FileNotFoundError as e:
            print(f"File not found: {file_path}")
    except Exception as e:
            print(f"An error occurred: {e}")
    
def read_json(file_path) -> list:
    """
    A function that reads a JSON file from the given file path and returns the data as a list.
    """
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

def read_xml(file_path) -> list:
    """
    Read an XML file and return a specific element from the parsed data.

    Parameters:
    - file_path (str): The path to the XML file to be read.

    Returns:
    - list: The specific element extracted from the XML data.
    """
    try:
        parser = XMLtoDict()
        with open(file_path, 'r') as f:
            data = parser.parse(f.read())
            root = data[list(data.keys())[0]]
            element = list(root.keys())[0]
            return root[element]
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
def read_sql(file_path) -> str:
    """
    A function that reads a SQL query from a file and returns it as a string.
    
    Parameters:
    - file_path (str): The path to the file containing the SQL query.
    
    Returns:
    - str: The SQL query read from the file.
    """
    try:
        with open(file_path, 'r') as f:
            query = f.read()
            return query
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(file_path):
    """
	Reads a file based on its format defined by the file path.
	Parameters:
	    file_path (str): The path to the file to be read.
	Returns:
	    The data read from the file based on its format.
	"""

    file_format = os.path.splitext(file_path)[1][1:]

    mapping_dict = {
        'csv': read_csv,
        'json': read_json,
        'xml': read_xml,
        'sql': read_sql
    }
    return mapping_dict[file_format](file_path)

