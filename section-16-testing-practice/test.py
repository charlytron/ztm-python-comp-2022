import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_things(self):
        test_param = 10
        result = main.do_things(test_param)
        self.assertEqual(result, 15)

    def test_do_things2(self):
        test_param = 'hawhuhhawhawhaw'
        result = main.do_things(test_param)
        self.assertIsInstance(result, ValueError)
        
    def test_do_things3(self):
      test_param = None
      result = main.do_things(test_param)
      self.assertEqual(result, 'Please use a number')


unittest.main()
