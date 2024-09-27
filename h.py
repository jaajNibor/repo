import tkinter as tk
from QRCodeGen import QRCodeGeneratorApp  # Importation du fichier QRCodeGen qui sert à generer le qrcode

import pytest

def app():
        # Création de la fenêtre Tkinter avant chaque test.
            root = tk.Tk()
            app_instance = QRCodeGeneratorApp(root)
        
        # Retourner l'instance de l'application pour les tests.
            yield app_instance
        
        # Teardown: Fermer la fenêtre Tkinter après chaque test.
            root.after(100, root.destroy)

        
            
            
            # Quitter la boucle principale
            # Mettre à jour la fenêtre pour appliquer les changements
            # Détruire la fenêtre après le test
        


class Test_QRCodeGen():
        #import de  pytest qui nous servira à tester le code QRCodeGen
    @pytest.fixture
    
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
    #not hasattr(app, 'qr_image') or
    def test_qr_code_url_vide(app):
            # Test pour une URL vide.
            app.entry.insert(0, "")  # Insérer une chaîne vide
            app.generate_qr_code()
            # Vérifier que la boîte d'avertissement est appelée.

            # Vérifier qu'aucun QR code n'a été généré.
            assert not hasattr(app, 'qr_image')