import unittest
from unitTesting import subtract_numbers

class testingFunction(unittest.TestCase):

    def testfirsttest(self):
        result = subtract_numbers(10, 7)
        self.assertEqual(result,3)
    
    def testsecondtest(self):
        result = subtract_numbers(2, 7)
        self.assertEqual(result,-5)
    
    def testthirdtest(self):
        result = subtract_numbers(5.5, 2.0)
        self.assertEqual(result,3.5)

if __name__ == '__main__':
    unittest.main()