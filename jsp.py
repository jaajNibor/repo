import tkinter as tk
from QRCodeGen import QRCodeGeneratorApp  # Importation du fichier QRCodeGen qui sert à générer le qrcode
import pytest
from unittest.mock import patch  # Import nécessaire pour utiliser mock

@pytest.fixture
def app():
    # Fixture pour créer une instance de l'application QRCodeGeneratorApp.
    root = tk.Tk()
    app_instance = QRCodeGeneratorApp(root)
    yield app_instance
    # Assure-toi que la fenêtre Tkinter est correctement détruite après le test.
    root.destroy()

def test_qr_code_generation(app):
    # Test pour vérifier que le QR code est généré correctement pour une URL valide.
    app.entry.insert(0, "https://google.com")
    app.generate_qr_code()
    # Vérifier que le QR code a été généré.
    assert app.qr_image is not None, "Le QR code n'a pas été généré correctement."

def test_qr_code_url_trop_longue(app):
    # Test pour une URL très longue.
    app.entry.insert(0, "ceci/est/une/url/tres/longue" + "haha" * 100)
    app.generate_qr_code()
    # Vérifier que le QR code a été généré malgré la longueur de l'URL.
    assert app.qr_image is not None, "Le QR code n'a pas été généré pour une URL très longue."

@patch('QRCodeGen.messagebox.showwarning')  # Mock du message d'avertissement
def test_qr_code_url_vide(app, mock_showwarning):
    # Test pour une URL vide.
    app.entry.insert(0, "")  # Insérer une chaîne vide
    app.generate_qr_code()
    # Vérifier que la boîte d'avertissement est appelée.
    mock_showwarning.assert_called_once_with("Avertissement", "Veuillez entrer une adresse URL pour générer un QR Code.")
    # Vérifier qu'aucun QR code n'a été généré.
    assert app.qr_image is None, "Un QR code a été généré alors que l'URL était vide."
