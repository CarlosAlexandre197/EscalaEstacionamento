from PyQt6.QtWidgets import QSpinBox
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
     QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QSpinBox
)


class TelaPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        self.configurar_janela()
        self.criar_componentes()
        self.criar_layout()
        self.preencher_tabela()

    def configurar_janela(self):
        self.setWindowTitle("Escala do Estacionamento")
        self.resize(1000, 650)

    def criar_componentes(self):

        self.spin_ano = QSpinBox()
        self.spin_ano.setMinimum(2025)
        self.spin_ano.setMaximum(2100)
        self.spin_ano.setValue(2026)

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

        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
    
    def preencher_tabela(self):

        dados = [
            ["Domingo", "Escola Bíblica", ""],
            ["Domingo", "Culto da Família", ""],
            ["Quarta", "Culto de Doutrina e Causas Impossíveis", ""],
            ["Sexta", "", ""],
            ["Sábado", "", ""]
        ]

        self.tabela.setRowCount(len(dados)) 
        
        for linha, dados_linha in enumerate(dados):

            for coluna, valor in enumerate(dados_linha):

                item = QTableWidgetItem(valor)

                self.tabela.setItem(
                    linha,
                    coluna,
                    item
                )   
            
    def criar_layout(self):

        layout_principal = QVBoxLayout()

        layout_principal.addWidget(self.lbl_titulo)

        # Layout do mês e ano
        layout_data = QHBoxLayout()

        layout_data.addWidget(QLabel("Mês:"))
        layout_data.addWidget(self.combo_mes)

        layout_data.addWidget(QLabel("Ano:"))
        layout_data.addWidget(self.spin_ano)

        layout_principal.addLayout(layout_data)

        # Layout dos botões
        layout_botoes = QHBoxLayout()

        layout_botoes.addWidget(self.btn_obreiros)
        layout_botoes.addWidget(self.btn_salvar)
        layout_botoes.addWidget(self.btn_pdf)

        layout_principal.addLayout(layout_botoes)

        layout_principal.addWidget(self.tabela)

        self.setLayout(layout_principal)