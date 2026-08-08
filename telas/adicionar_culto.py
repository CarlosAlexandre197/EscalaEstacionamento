from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)


class AdicionarCulto(QDialog):

    def __init__(self, obreiros=None):
        super().__init__()

        self.obreiros = obreiros or []

        self.configurar_janela()
        self.criar_componentes()
        self.criar_layout()
        self.criar_conexoes()

    def configurar_janela(self):
        self.setWindowTitle("Adicionar Culto")
        self.setFixedSize(400, 250)

    def criar_componentes(self):

        # ==========================================
        # Dia da semana
        # ==========================================

        self.lbl_dia = QLabel("Dia da semana")

        self.combo_dia = QComboBox()

        self.combo_dia.addItems([
            "Domingo",
            "Segunda",
            "Terça",
            "Quarta",
            "Quinta",
            "Sexta",
            "Sábado"
        ])

        # ==========================================
        # Nome do culto
        # ==========================================

        self.lbl_culto = QLabel("Nome do culto")

        self.edit_culto = QLineEdit()
        self.edit_culto.setPlaceholderText("Digite o nome do culto")

        # ==========================================
        # Obreiro
        # ==========================================

        self.lbl_obreiro = QLabel("Obreiro")

        self.combo_obreiro = QComboBox()

        # Limpa completamente o ComboBox
        self.combo_obreiro.clear()

        # Adiciona somente uma opção inicial
        self.combo_obreiro.addItem("Selecione...")

        # Adiciona os obreiros
        for nome in self.obreiros:

            nome = str(nome).strip()

            if nome and nome.lower() != "selecione...":
                self.combo_obreiro.addItem(nome)

        # ==========================================
        # Botões
        # ==========================================

        self.btn_salvar = QPushButton("Salvar")
        self.btn_cancelar = QPushButton("Cancelar")

    def criar_layout(self):

        layout = QVBoxLayout()

        layout.addWidget(self.lbl_dia)
        layout.addWidget(self.combo_dia)

        layout.addWidget(self.lbl_culto)
        layout.addWidget(self.edit_culto)

        layout.addWidget(self.lbl_obreiro)
        layout.addWidget(self.combo_obreiro)

        layout_botoes = QHBoxLayout()

        layout_botoes.addWidget(self.btn_salvar)
        layout_botoes.addWidget(self.btn_cancelar)

        layout.addLayout(layout_botoes)

        self.setLayout(layout)

    def criar_conexoes(self):

        self.btn_salvar.clicked.connect(self.salvar)
        self.btn_cancelar.clicked.connect(self.reject)

    def salvar(self):

        culto = self.edit_culto.text().strip()
        obreiro = self.combo_obreiro.currentText()

        # Verifica se o nome do culto foi informado
        if not culto:

            QMessageBox.warning(
                self,
                "Atenção",
                "Digite o nome do culto."
            )

            return

        # Verifica se o obreiro foi selecionado
        if obreiro == "Selecione...":

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione um obreiro."
            )

            return

        # Confirma o cadastro
        self.accept()

    def obter_dados(self):

        return {
            "dia": self.combo_dia.currentText(),
            "culto": self.edit_culto.text().strip(),
            "obreiro": self.combo_obreiro.currentText()
        }

