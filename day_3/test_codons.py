'''
Created on 07/02/2018

@author: Carolina
'''
import unittest
from module_3 import Codons

class Test(unittest.TestCase):
    
    def test_count_codons_by_sequence (self):
        codons = Codons()
        codons.count_codons_by_sequence('AAA')
        self.assertEqual(1,codons.dict_codon['AAA'])
        self.assertFalse('CCC' in codons.dict_codon)
        codons.count_codons_by_sequence('CCC')
        self.assertEqual(1,codons.dict_codon['AAA'])
        self.assertEqual(1,codons.dict_codon['CCC'])
        codons.count_codons_by_sequence('CCC')
        codons.count_codons_by_sequence('CCC')
        self.assertEqual(3,codons.dict_codon['CCC'])
    
    def test_count_codons(self):
        codons = Codons ()
        try:
            codons.count_codons ('kahsdjkhasdjkhas')
            self.fail('must fail')
        except:
            pass
if __name__ == '__main__':
    unittest.main()