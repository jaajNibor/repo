import unittest
import sys
import os

import pycountry

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '...\src')))
                        
from country import pays    


class Testpays(unittest.TestCase):
    def test_eu(self):
        self.assertEqual(pays("FR"),"Europe")

    def test_na(self):
        self.assertEqual(pays("US"),"North America")

    def test_NON(self):
        self.assertEqual(pays("DE"),"Africa")


if __name__=='__main__':
    unittest.main()
