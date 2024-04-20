import unittest

from Validate import is_passWord_valid
from Validate import is_ID_valid
#from Validate import addToTotal


class TestStringMethods(unittest.TestCase):
    # unit tests for password validation
    def test_passWord(self):
        self.assertTrue(is_passWord_valid("abcdefgh"))
        self.assertTrue(is_passWord_valid("123befhf"))

   
    #unit test for ID validation    
    def test_ID(self):
        self.assertTrue(is_ID_valid("12345"))
        
    
    

if __name__ == '__main__':
    unittest.main()