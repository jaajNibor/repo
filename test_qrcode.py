import tkinter as tk
from QRCodeGen import QRCodeGeneratorApp  # Importation de ton fichier QRCodeGen
import pytest

@pytest.fixture
def app():
    """Fixture pour créer une instance de l'application QRCodeGeneratorApp."""
    root = tk.Tk()
    app_instance = QRCodeGeneratorApp(root)
    return app_instance

def test_qr_code_generation(app):
    """Test simple pour vérifier que le QR code est généré correctement pour une URL valide."""
    # On simule l'entrée d'une URL valide dans le champ de saisie
    app.entry.insert(0, "https://google.com")
    
    # On appelle la fonction pour générer le QR code
    app.generate_qr_code()

    # On vérifie qu'une image de QRvCode a été créée et assignée à app.qr_image
    assert app.qr_image is not None, "Le QR code n'a pas été généré correctement."
