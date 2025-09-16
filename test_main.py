import unittest
from main import greet

class TestMain(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Jenkins CI"), "Hello, Jenkins CI!")

if __name__ == "__main__":
    unittest.main()
