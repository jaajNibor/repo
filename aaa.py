import tkinter as tk
from QRCodeGen import QRCodeGeneratorApp  # Importation du fichier QRCodeGen qui sert à generer le qrcode

import pytest
 #import de  pytest qui nous servira à tester le code QRCodeGen

@pytest.fixture
def app():
    #Fixture pour créer une instance de l'application QRCodeGeneratorApp.
    root = tk.Tk()
    app_instance = QRCodeGeneratorApp(root)
    return app_instance
    #on appelle donc QRCodeGeneratorApp du fichier



def test_qr_code_url_trop_longue(app):
    app.entry.insert(0, "ceci/est/une/url/tres/longue"+"haha"*100)
        
    try:
        app.generate_qr_code()
            # On vérifie qu'une image de QRCode a été générée
        assert app.qr_image is not None
    except Exception as e:
        pytest.fail(f"Le test a échoué avec l'exception : {e}, l'url est trop longue")
        # On vérifie qu'une image de QRCode a été créée et assignée à app.qr_image par le programme
    
