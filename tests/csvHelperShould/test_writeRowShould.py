import sys
sys.path.append('../../code')
import code.csvHelper as csvHelper

import unittest
import csv

class WriteRowShould(unittest.TestCase):

    def test_WriteOneRow_WithOneValue(self):
        filePath = 'tests/testHelpers/testData/SampleOutput.csv'
        definitions = {'Header One': { 'defaultValue': 'No Value Given'}}
        row = { 'Header One': 'Header One Value' }

        keysToPrint = list(definitions.keys())
        with open(filePath, 'w', newline='') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=keysToPrint)
            writer.writeheader()
            csvHelper.writeRow(row, definitions, writer)

        result = csvHelper.readRowsFrom(1, filePath)
        assert result[0]['Header One'] == 'Header One Value'

    def test_WriteOneRow_WithTwoValues(self):
        filePath = 'tests/testHelpers/testData/SampleOutput.csv'
        definitions = { 'Header One': {}, 'Header Two': {} }
        row = { 'Header One': 'Value One', 'Header Two': 'Value Two' }

        keysToPrint = list(definitions.keys())
        with open(filePath, 'w', newline='') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=keysToPrint)
            writer.writeheader()
            csvHelper.writeRow(row, definitions, writer)

        result = csvHelper.readRowsFrom(1, filePath)[0]
        assert result['Header One'] == 'Value One'
        assert result['Header Two'] == 'Value Two'


    # def test_ReadFiveRows(self):
    #     rows = csvHelper.readRowsFrom(5, 'tests/testHelpers/testData/SampleData.csv')
    #     assert len(rows) is 5

    # def test_ReadAllRows(self):
    #     rows = csvHelper.readRowsFrom(1000, 'tests/testHelpers/testData/SampleData.csv')
    #     assert len(rows) is 6

if __name__ == '__main__':
    unittest.main()