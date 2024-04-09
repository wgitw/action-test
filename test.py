import unittest
import main

class TestMain(unittest.TestCase):
    def test_print_hello(self):
        self.assertEqual(main.print_hello(), "Hello World")
        
if __name__ == '__main__':
    unittest.main()
