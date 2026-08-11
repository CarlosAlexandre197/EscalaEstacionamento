import webbrowser
import os
import subprocess


def enviar_pdf_whatsapp(caminho_pdf):

    if not caminho_pdf:
        return False

    if not os.path.exists(caminho_pdf):
        return False

    # Abre o WhatsApp Web
    webbrowser.open(
        "https://web.whatsapp.com/"
    )

    # Abre o Explorer com o PDF selecionado
    subprocess.Popen(
        [
            "explorer",
            "/select,",
            os.path.abspath(caminho_pdf)
        ]
    )

    return True