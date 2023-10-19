import unittest
import unitTesting

class testingFunction(unittest.TestCase):

    def firstTest(self):
        result = subtractionText.subtract_numbers(10, 7)
        self.assertEqual(result,3)
    
    def secondTest(self):
        result = subtractionText.subtract_numbers(2, 7)
        self.assertEqual(result,-5)
    
    def thirdTest(self):
        result = subtractionText.subtract_numbers(5.5, 2.0)
        self.assertEqual(result,3.0)
        
if __name__ == '__main__':
    unittest.main()