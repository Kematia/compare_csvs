import unittest
import csv
import os
from compare_csvs import read_csv, compare_csvs, write_csv

class TestCompareCSVs(unittest.TestCase):
    def setUp(self):
        self.file1 = 'test_file1.csv'
        self.file2 = 'test_file2.csv'
        self.output_file = 'test_output.csv'

        with open(self.file1, 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Value'])
            writer.writerow(['1', 'Alice', '100'])
            writer.writerow(['2', 'Bob', '200'])

        with open(self.file2, 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Value'])
            writer.writerow(['1', 'Alice', '100'])
            writer.writerow(['3', 'Charlie', '300'])

    def tearDown(self):
        os.remove(self.file1)
        os.remove(self.file2)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_read_csv(self):
        headers, data = read_csv(self.file1)
        self.assertEqual(headers, ['ID', 'Name', 'Value'])
        self.assertEqual(data, [['1', 'Alice', '100'], ['2', 'Bob', '200']])

    def test_compare_csvs(self):
        headers, differences = compare_csvs(self.file1, self.file2)
        self.assertEqual(headers, ['ID', 'Name', 'Value'])
        self.assertEqual(differences, [['2', 'Bob', '200'], ['3', 'Charlie', '300']])

    def test_write_csv(self):
        headers = ['ID', 'Name', 'Value']
        data = [['2', 'Bob', '200'], ['3', 'Charlie', '300']]
        write_csv(headers, data, self.output_file)

        with open(self.output_file, 'rb') as f:
            reader = csv.reader(f)
            out_headers = next(reader)
            out_data = [row for row in reader]

        self.assertEqual(out_headers, headers)
        self.assertEqual(out_data, data)

if __name__ == '__main__':
    unittest.main()