import add
import unittest

class TestSum(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(program.add(7, 11), 18)

if __name__ == '__main__':
    unittest.main()