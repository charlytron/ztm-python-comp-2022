import unittest
import main

class TestMain(unittest.TestCase):
  def test_bar_foo(self):
    test_param = 10
    result = main.bar_foo(test_param)
    self.assertEqual(result, 15)
    
  def test_bar_foo2(self):
    test_param = 'oogabooga'
    result = main.bar_foo(test_param)
    self.assertIsInstance(result, ValueError)
    
  def test_bar_foo3(self):
    test_param = None
    result = main.bar_foo(test_param)
    self.assertEqual(result, 'please enter number, yo')
    
  def test_bar_foo4(self):
    test_param = ''
    result = main.bar_foo(test_param)
    self.assertEqual(result, "please enter number, yo")
    
unittest.main()