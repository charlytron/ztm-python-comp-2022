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
    self.assertTrue(result, ValueError)
    
unittest.main()