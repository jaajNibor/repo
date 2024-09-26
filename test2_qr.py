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

    @patch('QRCodeGen.ImageTk.PhotoImage')  # on mock photoimage qui devrait normalement render l'image, pour éviter de l'afficher pendant le test
    def test_bonne_url(self, mock_photoimage):

        test_url = "http://Github/jaajNibor.repo"
        self.app.entry.get = MagicMock(return_value=test_url)

        # on génère le qr code (sans l'afficher)
        self.app.generate_qr_code()
#vérifier que le code a été généré
        self.assertIsNotNone(self.app.qr_image)
        mock_photoimage.assert_called_once()

    
    def url_tres_longue_ou_courte(self):
        #^^
        test_inputs = [
            "a",  # c'est court
            "http://ceci/est/une/url/tres/tres/longue/un/peu/trop/dailleurs/" + "a" * 1000, 
              # c'est long (je rajoute 1000 a derrière pour que ça dépasse)
        
            "url-qui-marche-pas"  # Invalid URL format
        ]

        for url in test_inputs:  #on check pour les urls invalides, longues et courtes
            with self.subTest(url=url):
                self.app.entry.get = MagicMock(return_value=url)
                self.app.generate_qr_code()

                # on vérifie que le code a été généré
                self.assertIsNotNone(self.app.qr_image)

        
               
 
if __name__ == '__main__':
    unittest.main()
