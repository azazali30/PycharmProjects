import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        num = 10
        result = main.do_stuff(num)
        self.assertEqual(result, 15)

    def test_do_stuff_error(self):
        num = "zaz"
        result = main.do_stuff(num)
        #self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)


unittest.main()