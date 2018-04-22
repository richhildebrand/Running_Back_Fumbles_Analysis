import sys
sys.path.append('../../code')
import code.csvHelper as csvHelper

import unittest

class ReadRowsFromShould(unittest.TestCase):

    def test_ReadTwoRows(self):
        rows = csvHelper.readRowsFrom(2, 'tests/testHelpers/testData/SampleData.csv')
        assert len(rows) is 2

if __name__ == '__main__':
    unittest.main()