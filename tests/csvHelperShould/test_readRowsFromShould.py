import sys
sys.path.append('../../code')
import code.csvHelper as csvHelper

import unittest

class ReadRowsFromShould(unittest.TestCase):

    def test_ReadTwoRows(self):
        rows = csvHelper.readRowsFrom(2, 'tests/testHelpers/testData/SampleData.csv')
        assert len(rows) is 2

    def test_ReadFiveRows(self):
        rows = csvHelper.readRowsFrom(5, 'tests/testHelpers/testData/SampleData.csv')
        assert len(rows) is 5

    def test_ReadAllRows(self):
        rows = csvHelper.readRowsFrom(1000, 'tests/testHelpers/testData/SampleData.csv')
        assert len(rows) is 6

if __name__ == '__main__':
    unittest.main()