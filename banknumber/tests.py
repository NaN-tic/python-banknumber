#This file is part of banknumber. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
'''
Unit test for banknumber
'''

import unittest
import banknumber

BANK_CODES = [
    ('ES', '21000813610123456789', True),
    ('ES', '21000813610123456780', False),
]

class BankNumberTest(unittest.TestCase):
    '''
    Test Case for banknumber
    '''

    def test_bank_numbers(self):
        '''
        Test Bank codes
        '''
        for code, number, result in BANK_CODES:
            if result:
                test = self.assert_
            else:
                test = self.assertFalse
            test(banknumber.check_code(code + number), code + number)

    def test_countries(self):
        '''
        Test countries
        '''
        banknumber.countries()

if __name__ == '__main__':
    unittest.main()
