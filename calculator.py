import unittest

def calculator(inputs):
    """
        - inputs: It includes the operand and the operator as a string
        - split through the inputs and loop through it to segregate the operands
    """
    value = []
    result = 0
    operarnd1 = 0
    operarnd2 = 0
    for i in inputs:        
        if i.isdigit() or (i.startswith('-') and i[1:].isdigit()):
            value.append(float(i))
        else:
            if len(value)>=2:
                operarnd2 = value.pop()
                operarnd1 = value.pop() 

            if i  == "+":
                result = operarnd1 + operarnd2
            elif i == "-":
                result = operarnd1 - operarnd2
            elif i == "*":
                result = operarnd1 * operarnd2
            elif i == "/":
                if operarnd2 ==0:
                    raise("Divisor should not be 0")
                result = operarnd1 / operarnd2
            else:
                raise("Unknown Operator")
            value.append(result)
            
    if len(value) == 1: 
        return value[0]
              

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