import unittest
from tkinter import * # Import the essential modules for the graphical user interface.
from tkinter import ttk
from refactor_3 import *
class calculate_test(unittest.TestCase):
     
   def test_sigleton(self):
      # Действие
      rt = Tk()
      rt1 = Tk()
      # Проверка
      assert(rt is not rt1)