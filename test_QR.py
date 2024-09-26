import unittest
import sys
import os
import unittest.mock
from unittest.mock import patch, MagicMock

import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '...\src')))
from QRCodeGen import QRCodeGeneratorApp
  

class TestQR(unittest.TestCase,):
    
    @patch('generate_qr_code.ImageTk.PhotoImage')  
    def test_generer_qr_code_avec_url_example(self, mock_photoimage):
        
        test_url = "http://example.com"
        self.app.entry.get = MagicMock(return_value=test_url)
            
        self.app.generate_qr_code()

        
        img = self.app.qr_image 
        self.assertIsNotNone(img)

       
    
    
    
    
    
    '''def test_qr(self):
        result=QRCodeGeneratorApp.generate_qr_code(self)
        self.assertNotEqual(result("aa"),None)
      '''

if __name__=='__main__':
    unittest.main()


