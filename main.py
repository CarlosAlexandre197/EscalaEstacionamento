import sys

from PyQt6.QtWidgets import QApplication

from database import Banco
from telas.tela_principal import TelaPrincipal


def main():

    app = QApplication(sys.argv)

    # Inicializa o banco de dados
    banco = Banco()

    # Abre a janela principal
    janela = TelaPrincipal(banco)
    janela.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()