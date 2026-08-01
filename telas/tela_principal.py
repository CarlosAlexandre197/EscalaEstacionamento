from telas.adicionar_culto import AdicionarCulto
from PyQt6.QtWidgets import QSpinBox
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QSpinBox,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox
)


class TelaPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        self.configurar_janela()
        self.criar_componentes()
        self.criar_layout()
        self.criar_conexoes()
        self.preencher_tabela()

    def configurar_janela(self):
        self.setWindowTitle("Escala do Estacionamento")
        self.resize(1000, 650)

    def criar_componentes(self):

        # ==========================================
        # Ano
        # ==========================================

        self.spin_ano = QSpinBox()
        self.spin_ano.setMinimum(2025)
        self.spin_ano.setMaximum(2100)
        self.spin_ano.setValue(2026)

        # ==========================================
        # Título
        # ==========================================

        self.lbl_titulo = QLabel("ESCALA DO ESTACIONAMENTO")
        self.lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # ==========================================
        # Mês
        # ==========================================

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

        # ==========================================
        # Botões
        # ==========================================

        self.btn_obreiros = QPushButton("👥 Obreiros")
        self.btn_salvar = QPushButton("💾 Salvar")
        self.btn_pdf = QPushButton("📄 Gerar PDF")
        self.btn_adicionar = QPushButton("➕ Adicionar Culto")
        self.btn_remover = QPushButton("🗑 Remover Culto")

        # Mesmo tamanho para todos os botões
        for botao in (
            self.btn_obreiros,
            self.btn_salvar,
            self.btn_pdf,
            self.btn_adicionar,
            self.btn_remover
        ):
            botao.setMinimumHeight(40)

        # ==========================================
        # Tabela
        # ==========================================

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

        self.tabela.setAlternatingRowColors(True)
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.verticalHeader().setDefaultSectionSize(35)
        self.tabela.setShowGrid(True)

        # ==========================================
        # Grupos
        # ==========================================

        self.grupo_dados = QGroupBox("📅 Dados da Escala")
        self.grupo_escala = QGroupBox("📋 Escala Mensal")
        
    def preencher_tabela(self):

        dados = [
            ["Domingo", "Escola Bíblica", ""],
            ["Domingo", "Culto da Família", ""],
            ["Quarta", "Culto de Doutrina e Causas Impossíveis", ""]
            
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

        # ==========================
        # Título
        # ==========================
        layout_principal.addWidget(self.lbl_titulo)

        # ==========================
        # Grupo Dados
        # ==========================
        layout_data = QHBoxLayout()

        layout_data.addWidget(QLabel("Mês:"))
        layout_data.addWidget(self.combo_mes)

        layout_data.addSpacing(30)

        layout_data.addWidget(QLabel("Ano:"))
        layout_data.addWidget(self.spin_ano)

        layout_data.addStretch()

        self.grupo_dados.setLayout(layout_data)

        layout_principal.addWidget(self.grupo_dados)

        # ==========================
        # Grupo Escala
        # ==========================
        layout_tabela = QVBoxLayout()

        layout_tabela.addWidget(self.tabela)

        layout_cultos = QHBoxLayout()

        layout_cultos.addWidget(self.btn_adicionar)
        layout_cultos.addWidget(self.btn_remover)

        layout_tabela.addLayout(layout_cultos)

        self.grupo_escala.setLayout(layout_tabela)

        layout_principal.addWidget(self.grupo_escala)

        # ==========================
        # Botões inferiores
        # ==========================
        layout_botoes = QHBoxLayout()

        layout_botoes.addWidget(self.btn_obreiros)

        layout_botoes.addStretch()

        layout_botoes.addWidget(self.btn_salvar)
        layout_botoes.addWidget(self.btn_pdf)

        layout_principal.addLayout(layout_botoes)

        self.setLayout(layout_principal)
        
    def criar_conexoes(self):

        self.btn_adicionar.clicked.connect(self.adicionar_culto)
        self.btn_remover.clicked.connect(self.remover_culto)
        
    def adicionar_culto(self):
    
        janela = AdicionarCulto()
        janela.exec()

    def remover_culto(self):
        print("Remover culto")
        
    