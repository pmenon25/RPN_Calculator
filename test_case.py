import unittest
from calculator import calculator 

class CalculatorTest(unittest.TestCase):   
    def test_calculator_positive(self):
        self.calculator = calculator('3 4 +')
        self.assertEqual(self.calculator, 7)
    def test_calculator_negative(self):
        self.calculator = calculator('3 -4 +')
        self.assertEqual(self.calculator, -1)
    def test_calculator_multiple(self):
        self.calculator = calculator('3 4 + 9 - 10 / 4 *' )
        self.assertEqual(self.calculator, -0.8)