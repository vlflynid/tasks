import unittest
from unittest.mock import patch, mock_open
from writers import write_file, WritersException

class TestWriteFile(unittest.TestCase):

    @patch('writers.write_data_to_json')
    def test_write_json_file(self, mock_write_data_to_json):
        data = [{"key": "value"}]
        file_name = "test"
        format = "json"
        mock_write_data_to_json.return_value = "Success"
        
        result = write_file(data, file_name, format)
        
        self.assertEqual(result, "Success")

    @patch('writers.write_data_to_xml')
    def test_write_xml_file(self, mock_write_data_to_xml):
        data = {"key": "value"}
        file_name = "test"
        format = "xml"
        mock_write_data_to_xml.return_value = "Success"
        
        result = write_file(data, file_name, format)
        
        self.assertEqual(result, "Success")

    @patch('writers.write_data_to_csv')
    def test_write_csv_file(self, mock_write_data_to_csv):
        data = [{"key": "value"}]
        file_name = "test"
        format = "csv"
        mock_write_data_to_csv.return_value = "Success"
        
        result = write_file(data, file_name, format)
        
        self.assertEqual(result, "Success")

    def test_unsupported_format_exception(self):
        data = {"key": "value"}
        file_name = "test"
        format = "unsupported_format"
        
        with self.assertRaises(WritersException):
            write_file(data, file_name, format)

if __name__ == '__main__':
    unittest.main()