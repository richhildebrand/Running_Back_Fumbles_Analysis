import sys
sys.path.append('../../code')
import code.csvHelper as csvHelper

import unittest
import csv

class EnsureKeysShould(unittest.TestCase):
    def test_AddMissingKey(self):
        definitions = {'Header One': {'defaultValue': 'no value given'}}
        dictionary = { }

        dictionary = csvHelper.ensureKeys(dictionary, definitions)

        assert dictionary['Header One'] == 'no value given'

    def test_NotOverwriteFoundKey(self):
        definitions = {'Header One': {'defaultValue': 'no value given'}}
        dictionary = { 'Header One': 'Given Value'}

        dictionary = csvHelper.ensureKeys(dictionary, definitions)

        assert dictionary['Header One'] == 'Given Value'

if __name__ == '__main__':
    unittest.main()