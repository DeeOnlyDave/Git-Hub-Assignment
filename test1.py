import add
import unittest

class TestSum(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(program.add(2, 4), 6)

if __name__ == '__main__':
    unittest.main()