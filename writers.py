import os
import json
import csv
from dict2xml import dict2xml
import logging

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
        logging.error(f"An error occurred: {e}")

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
            xml_data = dict2xml(data)
            f.write(xml_data)
            logging.info(f"Successfully wrote XML data to {file_path}")
    except Exception as e:
        logging.error(f"Error writing XML data to {file_path}: {e}")

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
        with open(file_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            for item in data:
                writer.writerow(item)
            logging.info(f"Successfully wrote CSV data to {file_path}")
    except Exception as e:
        logging.error(f"Error writing CSV data to {file_path}: {e}")

def write_file(data: list, file_name: str, format: str):
    """
    A function that writes data to a file in the specified format.

    Parameters:
    - data (list): The data to be written to the file.
    - file_name (str): The name of the file to write the data to.
    - format (str): The format in which the data should be written to the file.

    Returns:
    The result of writing the data to the file.
    """
    
    mapping_dict = {
        'json': write_data_to_json,
        'xml': write_data_to_xml,
        'csv': write_data_to_csv
    }

    if(format in mapping_dict.keys()):
        if not os.path.exists(f"analysed/{format}"):
            os.makedirs(f"analysed/{format}")
        file_path = f"analysed/{format}/{file_name}.{format}"
        logging.info(f"Writing {file_name} in {format} format to {file_path}")
        try:
            result = mapping_dict[format](data, file_path)
            logging.info(f"Successfully wrote {file_name} in {format} format to {file_path}")
            return result
        except Exception as e:
            logging.error(f"Error writing {file_name} in {format} format to {file_path}: {e}")
            raise
    else:
        logging.error(f"Invalid format: {format}")
        raise ValueError(f"Invalid format: {format}")

