import os
import json
import csv
from dict2xml import dict2xml
def write_data_to_json(data: dict, file_path: str):
        """
        A function that writes data to a JSON file.

        Parameters:
            data (dict): The data to be written to the JSON file.
            file_path (str): The file path where the data will be written.

        Returns:
            None
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"An error occurred: {e}")

def write_data_to_xml(data: dict, file_path: str):
    """
    Write data to an XML file.

    Parameters:
    - data (dict): The data to be written to the XML file.
    - file_path (str): The file path where the data will be written.

    Returns:
    None
    """
    try:
        with open(file_path, 'w') as f:
            f.write(dict2xml(data))
    except Exception as e:
        print(f"An error occurred: {e}")

def write_data_to_csv(data: dict, file_path: str):
    """
    Write data to a CSV file.

    Args:
        data (dict): The data to be written to the CSV file.
        file_path (str): The file path of the CSV file.

    Returns:
        None
    """
    try:
        with open(file_path, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            for item in data:
                writer.writerow(item)
    except Exception as e:
        print(f"An error occurred: {e}")

def write_file(data: str, file_name: str, format: str):
    """
	Write data to a file in the specified format.
	Parameters:
	- data (str): The data to write to the file.
	- file_name (str): The name of the file to write the data to.
	- format (str): The format in which to write the data (json, xml, csv).
	Returns:
	- The result of writing the data to the file in the specified format.
	"""
    
    mapping_dict = {
        'json': write_data_to_json,
        'xml': write_data_to_xml,
        'csv': write_data_to_csv
    }

    if not os.path.exists(f"analysed/{format}"):
        os.makedirs(f"analysed/{format}")
    file_path = f"analysed/{format}/{file_name}.{format}"

    return mapping_dict[format](data, file_path)

