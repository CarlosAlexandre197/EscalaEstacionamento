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

        self.setWindowTitle("Escala do Estacionamento")

        self.resize(900, 600)

        layout = QVBoxLayout()

        titulo = QLabel("ESCALA DO ESTACIONAMENTO")

        layout.addWidget(titulo)

        self.setLayout(layout)