import unittest
from app.math_utils import sum_numbers


class TestMathUtils(unittest.TestCase):

    def test_sum_positive(self):
        self.assertEqual(sum_numbers(5, 10), 15)

    def test_sum_negative(self):
        self.assertEqual(sum_numbers(-5, -5), -10)

    def test_sum_mixed(self):
        self.assertEqual(sum_numbers(-5, 5), 0)


if __name__ == "__main__":
    unittest.main()
