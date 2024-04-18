import unittest

from Validate import is_passWord_valid
from Validate import is_ID_valid
#from Validate import addToTotal


class TestStringMethods(unittest.TestCase):
    # unit tests for password validation
    def test_passWord(self):
        self.assertTrue(is_passWord_valid("abcdefgh"))
        self.assertTrue(is_passWord_valid("123befhf"))

   
        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    

if __name__ == '__main__':
    unittest.main()