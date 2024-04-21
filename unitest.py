import unittest
from your_script_name import generate_random_numbers, sum_and_print

class TestRandomSum(unittest.TestCase):

    def test_generate_random_numbers(self):
        num1, num2 = generate_random_numbers()
        self.assertTrue(isinstance(num1, int))
        self.assertTrue(isinstance(num2, int))

    def test_sum_and_print(self):
        total = sum_and_print(10, 20)
        self.assertEqual(total, 30)

if __name__ == '__main__':
    unittest.main()
