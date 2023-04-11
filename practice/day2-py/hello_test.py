import unittest
import hello


class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = hello.main_func(1, 2)
        self.assertEqual(result, 30)
    
    def test_add_negative_numbers(self):
        result = hello.main_func(-1, -2)
        self.assertEqual(result, -30)
    
    def test_add_mixed_numbers(self):
        result = hello.main_func(2, -3)
        self.assertEqual(result, -10)


class TestReturnFormattedStrings(unittest.TestCase):
    def test_returned_string(self):
        result = hello.return_string('Abracadabra')
        self.assertTrue(result, 'Abracadabra.')

if __name__ == '__main__':
    unittest.main()
