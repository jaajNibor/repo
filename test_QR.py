import unittest
import sys
import os
from unittest.mock import patch

import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '...\src')))
from QRCode import QRCodeGeneratorApp




    

'''class TestQR(unittest.TestCase):
    def test_qr(self):
        self.assertEqual(generate_qr_code("FR"),"Europe")
'''

if __name__=='__main__':
    unittest.main()
#assert pays('FR') == 'Europe'
'''if __name__=='__moyenne__':
    unittest.main()'''