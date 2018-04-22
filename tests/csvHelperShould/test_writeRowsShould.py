import sys
sys.path.append('../../code')
import code.csvHelper as csvHelper

import unittest
import csv

class WriteRowsShould(unittest.TestCase):
    filePath = 'tests/testHelpers/testData/SampleOutput.csv'

    def test_WriteOneRow_WithOneValue(self):
        definitions = {'Header One': {}}
        rows = {
            'id_1': { 'Header One': 'Row One' },
            'id_2': { 'Header One': 'Row Two' },
            'id_3': { 'Header One': 'Row Three' }
        }

        csvHelper.writeRows(rows, definitions, self.filePath)

        result = csvHelper.readRowsFrom(3, self.filePath)
        assert result[0]['Header One'] == 'Row One'
        assert result[1]['Header One'] == 'Row Two'
        assert result[2]['Header One'] == 'Row Three'

if __name__ == '__main__':
    unittest.main()