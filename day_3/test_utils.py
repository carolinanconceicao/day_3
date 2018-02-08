'''
Created on 07/02/2018

@author: Carolina
'''
import unittest
import utils

class Test(unittest.TestCase):

    def test_is_float(self):
        self.assertIsNone(utils.is_float('value'))
        self.assertEqual(10.0,utils.is_float('10'))
        self.assertEqual(10.0, utils.is_float(10))
        self.assertIsNone(utils.is_number('value'))
        self.assertEqual(10,utils.is_number('10'))
        self.assertEqual(10, utils.is_number(10))
        
    def runTest(self):
        self.test_is_float()
        pass
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test is float']
    unittest.main()