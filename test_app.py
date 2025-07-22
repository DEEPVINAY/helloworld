import unittest
from app import helloworld

class TestHelloWorld(unittest.TestCase):
    def test_helloworld_output(self):
        self.assertEqual(helloworld(), "HelloWorld")

if __name__ == "__main__":
    unittest.main()
