import unittest
import math
import sc_calculator  # Import your correct module

class TestCalculator(unittest.TestCase):
    def test_square_root(self):
        self.assertAlmostEqual(sc_calculator.square_root(9), 3, places=5)
        self.assertAlmostEqual(sc_calculator.square_root(16), 4, places=5)

    def test_factorial(self):
        self.assertEqual(sc_calculator.factorial(5), 120)
        self.assertEqual(sc_calculator.factorial(0), 1)

    def test_natural_log(self):
        self.assertAlmostEqual(sc_calculator.natural_log(math.e), 1, places=5)
        self.assertAlmostEqual(sc_calculator.natural_log(1), 0, places=5)

    def test_power(self):
        self.assertEqual(sc_calculator.power(2, 3), 8)
        self.assertEqual(sc_calculator.power(5, 0), 1)

if __name__ == "__main__":
    unittest.main()

