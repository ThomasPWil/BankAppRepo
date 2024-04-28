# unit tests are conducted here


import unittest

from Validate import is_passWord_valid
from Validate import is_ID_valid
from Validate import is_Firstname_Valid
from Validate import is_Lastname_Valid
from Validate import isIntialDeposValid
#from Validate import addToTotal


class TestStringMethods(unittest.TestCase):
    # unit tests for password validation
    def test_passWord(self):
        self.assertTrue(is_passWord_valid("abcdefgh"))
        self.assertTrue(is_passWord_valid("123befhf"))

   
    #unit test for ID validation    
    def test_ID(self):
        self.assertTrue(is_ID_valid("12345"))

    #unit test for first name
    def testNameFirst(self):
        self.assertTrue(is_Firstname_Valid("thomas"))
    

    # unit test for last name
    def testNameLast(self):
        self.assertTrue(is_Lastname_Valid("wilson"))
        self.assertTrue(is_Lastname_Valid("Wilson"))

    def testIntialDepos(self):
        self.assertTrue(isIntialDeposValid("1"))

    def testIntialDepos2(self):
        self.assertFalse(isIntialDeposValid("a"))
    
    

if __name__ == '__main__':
    unittest.main()