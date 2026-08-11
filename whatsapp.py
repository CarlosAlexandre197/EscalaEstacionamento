import webbrowser
import os


def abrir_whatsapp():

    webbrowser.open(
        "https://web.whatsapp.com/"
    )


def enviar_pdf_whatsapp(caminho_pdf):

    if not caminho_pdf:
        return False

    if not os.path.exists(caminho_pdf):
        return False

    webbrowser.open(
        "https://web.whatsapp.com/"
    )

    return True