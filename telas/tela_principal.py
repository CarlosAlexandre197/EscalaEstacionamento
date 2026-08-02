from style import (
    JANELA,
    TITULO,
    BOTAO_PRIMARIO,
    BOTAO_SECUNDARIO,
    TABELA,
    COMBOBOX,
    SPINBOX
)

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
        self.aplicar_estilos()
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

        # ==========================================
        # Layout Principal
        # ==========================================

        layout_principal = QVBoxLayout()
        layout_principal.setSpacing(15)
        layout_principal.setContentsMargins(20, 20, 20, 20)

        # ==========================================
        # Título
        # ==========================================

        layout_principal.addWidget(self.lbl_titulo)

        # ==========================================
        # Grupo Dados da Escala
        # ==========================================

        layout_dados = QHBoxLayout()

        layout_dados.addWidget(QLabel("Mês:"))
        layout_dados.addWidget(self.combo_mes)

        layout_dados.addSpacing(30)

        layout_dados.addWidget(QLabel("Ano:"))
        layout_dados.addWidget(self.spin_ano)

        layout_dados.addStretch()

        self.grupo_dados.setLayout(layout_dados)

        layout_principal.addWidget(self.grupo_dados)

        # ==========================================
        # Grupo Escala
        # ==========================================

        layout_escala = QVBoxLayout()

        layout_escala.addWidget(self.tabela)

        layout_cultos = QHBoxLayout()

        layout_cultos.addWidget(self.btn_adicionar)
        layout_cultos.addWidget(self.btn_remover)
        layout_cultos.addStretch()

        layout_escala.addLayout(layout_cultos)

        self.grupo_escala.setLayout(layout_escala)

        layout_principal.addWidget(self.grupo_escala)

        # ==========================================
        # Botões Inferiores
        # ==========================================

        layout_botoes = QHBoxLayout()

        layout_botoes.addWidget(self.btn_obreiros)

        layout_botoes.addStretch()

        layout_botoes.addWidget(self.btn_salvar)
        layout_botoes.addWidget(self.btn_pdf)

        layout_principal.addLayout(layout_botoes)

        self.setLayout(layout_principal)
        
    def aplicar_estilos(self):

        # Estilo da janela
        self.setStyleSheet(JANELA)

        # Título
        self.lbl_titulo.setStyleSheet(TITULO)

        # Campos
        self.combo_mes.setStyleSheet(COMBOBOX)
        self.spin_ano.setStyleSheet(SPINBOX)

        # Tabela
        self.tabela.setStyleSheet(TABELA)

        # Botões principais
        self.btn_salvar.setStyleSheet(BOTAO_PRIMARIO)
        self.btn_pdf.setStyleSheet(BOTAO_PRIMARIO)

        # Botões secundários
        self.btn_obreiros.setStyleSheet(BOTAO_SECUNDARIO)
        self.btn_adicionar.setStyleSheet(BOTAO_SECUNDARIO)
        self.btn_remover.setStyleSheet(BOTAO_SECUNDARIO)
        
    def criar_conexoes(self):

        self.btn_adicionar.clicked.connect(self.adicionar_culto)
        self.btn_remover.clicked.connect(self.remover_culto)
        
    def adicionar_culto(self):
    
        janela = AdicionarCulto()
        janela.exec()

    def remover_culto(self):
        print("Remover culto")
        
    