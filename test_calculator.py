import unittest

from calculator import InvalidCalculatorParamsError, calculate


class TestCalculator(unittest.TestCase):
    def test_pass_not_existing_region(self):
        with self.assertRaises(InvalidCalculatorParamsError):
            calculate(100, "NOT_REGION")

    def test_pass_negative_price(self):
        with self.assertRaises(InvalidCalculatorParamsError):
            calculate(-100500, "CA")

    def test_pass_zero_price(self):
        self.assertEqual(calculate(0, "AL"), 0)

    def test_pass_big_price(self):
        expected = 100500 * (100 - 15) / 100 * (100 + 4) / 100
        self.assertEqual(calculate(100500, "AL"), expected)

    def test_pass_lowest_reference_price(self):
        expected = 1000 * (100 - 3) / 100 * (100 + 4) / 100
        self.assertEqual(calculate(1000, "AL"), expected)

    def test_pass_highest_reference_price(self):
        expected = 50000 * (100 - 15) / 100 * (100 + 4) / 100
        self.assertEqual(calculate(50000, "AL"), expected)

    def test_pass_reference_price_in_the_middle(self):
        expected = 7000 * (100 - 7) / 100 * (100 + 4) / 100
        self.assertEqual(calculate(7000, "AL"), expected)

    def test_pass_intermediate_price(self):
        expected = 20000 * (100 - 10) / 100 * (100 + 4) / 100
        self.assertEqual(calculate(20000, "AL"), expected)


if __name__ == "__main__":
    unittest.main()
