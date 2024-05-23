import numpy as np

class calculate():
    
    def addition(number1, number2):
        return number1 + number2
    def substraction(number1, number2):
        return number1 - number2
    def multiplication(number1, number2):
        return number1 * number2
    def division(number1, number2):
        return np.round(int((number1 / number2) * 1000000 + 0.5) / 1000000.0, 3)
    def factorial(self, number):
        if number == 0:
            return 1
        else:
            return number * self.factorial(number - 1)