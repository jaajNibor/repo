import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import qrcode
import os
from QRCodeGen import QRCodeGeneratorApp  

class TestQRCodeGeneratorApp(unittest.TestCase):

    def setUp(self):
        # Set up the tkinter root and the app instance
        self.root = tk.Tk()  
        self.app = QRCodeGeneratorApp(self.root)

    def tearDown(self):
        # Destroy the tkinter root after each test to avoid interference
        self.root.destroy()

    @patch('qrcodegen.messagebox.showwarning')  # Mock messagebox.showwarning
    def url_vide(self, mock_showwarning):
        #test avec champs url vide
        
        self.app.entry.get = MagicMock(return_value="")

        #génération du code
        self.app.generate_qr_code()

        # Asssert que pas champs url vide donne un aertissement 
        mock_showwarning.assert_called_once_with("Avertissement", "Veuillez entrer une adresse URL pour générer un QR Code.")

    @patch('your_module.ImageTk.PhotoImage')  # on mock photoimage qui devrait normalement render l'image, pour éviter de l'afficher pendant le test
    def test_bonne_url(self, mock_photoimage):

        test_url = "http://Github/jaajNibor.repo"
        self.app.entry.get = MagicMock(return_value=test_url)

        # on génère le qr code (sans l'afficher)
        self.app.generate_qr_code()

        # Ensure that a QR code image was generated and assigned to the label
        self.assertIsNotNone(self.app.qr_image)
        mock_photoimage.assert_called_once()

        # Optionally, you can save the QR code for manual verification
        qr_image_path = "test_qr_code_valid.png"
        self.app.qr_image._PhotoImage__photo.write(qr_image_path)
        print(f"Valid URL QR code generated and saved as {qr_image_path}")

    def test_generate_real_qr_code_edge_case_inputs(self):
        """Test case where edge-case inputs are provided, like a very short or very long URL."""
        test_inputs = [
            "a",  # Single character
            "http://example.com/very-very-long-url/" + "a" * 1000,  # Long URL
            "ftp://example.com",  # Non-HTTP/HTTPS scheme
            "invalid-url"  # Invalid URL format
        ]

        for url in test_inputs:
            with self.subTest(url=url):
                self.app.entry.get = MagicMock(return_value=url)
                self.app.generate_qr_code()

                # Ensure that a QR code image is generated
                self.assertIsNotNone(self.app.qr_image)

                # Optional: Save the QR code for manual verification
                qr_image_path = f"test_qr_code_edge_{url[:10]}.png"
                self.app.qr_image._PhotoImage__photo.write(qr_image_path)
                print(f"Edge case URL QR code generated and saved as {qr_image_path}")

    def test_generate_real_qr_code_non_ascii_characters(self):
        """Test case where a URL contains non-ASCII characters, such as Unicode characters."""
        test_url = "https://example.com/こんにちは"
        self.app.entry.get = MagicMock(return_value=test_url)

        # Call the QR code generation method
        self.app.generate_qr_code()

        # Ensure that a QR code image is generated
        self.assertIsNotNone(self.app.qr_image)

        # Optional: Save the QR code for manual verification
        qr_image_path = "test_qr_code_unicode.png"
        self.app.qr_image._PhotoImage__photo.write(qr_image_path)
        print(f"Unicode URL QR code generated and saved as {qr_image_path}")

    def test_invalid_image_saving(self):
        """Test invalid image handling (e.g., failing to save the QR code image)."""
        test_url = "http://example.com"
        self.app.entry.get = MagicMock(return_value=test_url)

        # Call the QR code generation method
        self.app.generate_qr_code()

        # Simulate failure in saving the QR code image
        with patch.object(self.app.qr_image._PhotoImage__photo, 'write', side_effect=OSError("Unable to save image")):
            with self.assertRaises(OSError):
                self.app.qr_image._PhotoImage__photo.write("invalid_path.png")

if __name__ == '__main__':
    unittest.main()
