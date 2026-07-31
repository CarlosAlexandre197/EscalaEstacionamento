from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class TelaPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        self.configurar_janela()

    def configurar_janela(self):

        self.setWindowTitle("Escala da Portaria")

        self.resize(900, 600)

        layout = QVBoxLayout()

        titulo = QLabel("ESCALA DA PORTARIA")

        layout.addWidget(titulo)

        self.setLayout(layout)