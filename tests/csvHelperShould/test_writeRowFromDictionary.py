import sys
sys.path.append('../../code')
import code.csvHelper as csvHelper

import unittest
import csv

class ReadRowsFromShould(unittest.TestCase):

    def test_WriteOneRow(self):
        print('pass')
    #     filePath = 'tests/testHelpers/testData/SampleOutput.csv'
    #     definitions = { 'foo': {'key': 'FooKey', 'defaultValue': 'No Value Given'} }
    #     dictionary = { 'foo': 'FooValue' }

    #     with open(filePath, 'w', newline='') as csv_file:
    #         writer = csv.writer(csv_file)
    #         csvHelper.writeRowFromDictionary(definitions, dictionary, writer)

    #     result = csvHelper.readRowsFrom(1, filePath)


    # def test_ReadFiveRows(self):
    #     rows = csvHelper.readRowsFrom(5, 'tests/testHelpers/testData/SampleData.csv')
    #     assert len(rows) is 5

    # def test_ReadAllRows(self):
    #     rows = csvHelper.readRowsFrom(1000, 'tests/testHelpers/testData/SampleData.csv')
    #     assert len(rows) is 6

if __name__ == '__main__':
    unittest.main()