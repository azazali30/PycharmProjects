import unittest
import main


class TestMain(unittest.TestCase):
    def test_guess_game(self):
        num = 10
        result = main.guess_game(10,10)
        self.assertTrue(result)



unittest.main()