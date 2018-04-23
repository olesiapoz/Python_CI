import unittest
import app

class MyUnitTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(app.my_function(1,1),2)
        self.assertEqual(app.my_function(1,2.2),3.2)

if __name__ == '__main__' :
    unittest.main()