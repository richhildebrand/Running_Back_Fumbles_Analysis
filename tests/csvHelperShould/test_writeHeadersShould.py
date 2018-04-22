import sys
sys.path.append('../../code')
import code.csvHelper as csvHelper

import unittest
import csv

class WriteHeadersFromDefinitionsShould(unittest.TestCase):

    def test_WritOneHeader(self):
        filePath = 'tests/testHelpers/testData/SampleOutput.csv'
        definitions = [{'key': 'Header One', 'defaultValue': 'No Value Given'}]

        with open(filePath, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            csvHelper.writeHeadersFromDefinitions(definitions, writer)

        result = csvHelper.readRowsFrom(1, filePath)
        print(result)

    def test_WritThreeHeaders(self):
        filePath = 'tests/testHelpers/testData/SampleOutput.csv'
        definitions = [
            {'key': 'Header One', 'defaultValue': 'No Value Given'},
            {'key': 'Header Two', 'defaultValue': 'No Value Given'},
            {'key': 'Header Three', 'defaultValue': 'No Value Given'}
        ]

        with open(filePath, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            csvHelper.writeHeadersFromDefinitions(definitions, writer)

        result = csvHelper.readRowsFrom(1, filePath)
        print(result)


    # def test_ReadFiveRows(self):
    #     rows = csvHelper.readRowsFrom(5, 'tests/testHelpers/testData/SampleData.csv')
    #     assert len(rows) is 5

    # def test_ReadAllRows(self):
    #     rows = csvHelper.readRowsFrom(1000, 'tests/testHelpers/testData/SampleData.csv')
    #     assert len(rows) is 6

if __name__ == '__main__':
    unittest.main()