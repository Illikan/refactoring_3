import unittest
from tkinter import * # Import the essential modules for the graphical user interface.
from tkinter import ttk
from calculate import calculate
class calculate_test(unittest.TestCase):
     
   def test_sigleton(self):
      # Действие
      rt = Tk()
      rt1 = Tk()
      # Проверка
      assert(rt is not rt1)
      
   def test_addition(self):
      # Подготовка
      num1 = -2
      num2 = -3
      # Действие
      result = calculate.addition(num1, num2)
      # Проверка
      assert(result == -5)
      
   def test_substraction(self):
      # Подготовка
      num1 = -2
      num2 = -3
      # Действие
      result = calculate.substraction(num1, num2)
      # Проверка
      assert(result == 1)
      
   def test_multiplication(self):
      # Подготовка
      num1 = -2
      num2 = -3
      # Действие
      result = calculate.multiplication(num1, num2)
      # Проверка
      assert(result == 6)
      
   def test_division(self):
      # Подготовка
      num1 = -2
      num2 = -3
      # Действие
      result = calculate.division(num1, num2)
      # Проверка
      assert(result == 0.667)
      