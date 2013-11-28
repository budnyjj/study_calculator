#!/usr/bin/python2

import unittest
import calculator.calculator as calculator

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator.Calculator()

    def testExampleStrings(self):
        iExpr = "1*4+3.3/(3+.3)*3(sqrt(4))/(sin(0)+1)"
        self.assertEqual(self.calculator.calculate(iExpr), 10)
        iExpr = "10*e^0*log10(.4*-5/-0.1-10)--abs(-53//10)+-5"
        self.assertEqual(self.calculator.calculate(iExpr), 11) # exactly!

if __name__ == '__main__':
    unittest.main()
