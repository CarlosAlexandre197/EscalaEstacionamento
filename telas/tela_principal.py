from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QComboBox,
    QTableWidget,
    QHeaderView
)


class TelaPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        self.configurar_janela()
        self.criar_componentes()
        self.criar_layout()

    def configurar_janela(self):
        self.setWindowTitle("Escala do Estacionamento")
        self.resize(1000, 650)

    def criar_componentes(self):

        self.lbl_titulo = QLabel("ESCALA DO ESTACIONAMENTO")
        self.lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.combo_mes = QComboBox()
        self.combo_mes.addItems([
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ])

        self.btn_obreiros = QPushButton("Obreiros")
        self.btn_salvar = QPushButton("Salvar")
        self.btn_pdf = QPushButton("Gerar PDF")

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels([
            "Dia",
            "Culto",
            "Obreiro"
        ])

        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        

    def criar_layout(self):

        layout_principal = QVBoxLayout()

        layout_principal.addWidget(self.lbl_titulo)
        layout_principal.addWidget(self.combo_mes)

        layout_botoes = QHBoxLayout()

        layout_botoes.addWidget(self.btn_obreiros)
        layout_botoes.addWidget(self.btn_salvar)
        layout_botoes.addWidget(self.btn_pdf)

        layout_principal.addLayout(layout_botoes)

        layout_principal.addWidget(self.tabela)

        self.setLayout(layout_principal)