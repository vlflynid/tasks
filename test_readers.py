import unittest
from unittest.mock import patch, mock_open
from readers import read_file, read_csv, read_json, read_xml, read_sql, read_yaml

class TestReadFile(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='csv data')
    def test_read_csv_file(self, mock_open):
        file_path = 'test.csv'
        result = read_file(file_path)
        mock_open.assert_called_once_with(file_path, 'r')
        self.assertEqual(result, read_csv(file_path))

    @patch('builtins.open', new_callable=mock_open, read_data='json data')
    def test_read_json_file(self, mock_open):
        file_path = 'test.json'
        result = read_file(file_path)
        mock_open.assert_called_once_with(file_path, 'r')
        self.assertEqual(result, read_json(file_path))

    @patch('builtins.open', new_callable=mock_open, read_data='xml data')
    def test_read_xml_file(self, mock_open):
        file_path = 'test.xml'
        result = read_file(file_path)
        mock_open.assert_called_once_with(file_path, 'r')
        self.assertEqual(result, read_xml(file_path))

    @patch('builtins.open', new_callable=mock_open, read_data='sql data')
    def test_read_sql_file(self, mock_open):
        file_path = 'test.sql'
        result = read_file(file_path)
        mock_open.assert_called_once_with(file_path, 'r')
        self.assertEqual(result, read_sql(file_path))

    @patch('builtins.open', new_callable=mock_open, read_data='yaml data')
    def test_read_yaml_file(self, mock_open):
        file_path = 'test.yaml'
        result = read_file(file_path)
        mock_open.assert_called_once_with(file_path, 'r')
        self.assertEqual(result, read_yaml(file_path))

    def test_unsupported_format_exception(self):
        file_path = 'test.txt'  # Unsupported format
        with self.assertRaises(ValueError):
            read_file(file_path)

if __name__ == '__main__':
    unittest.main()