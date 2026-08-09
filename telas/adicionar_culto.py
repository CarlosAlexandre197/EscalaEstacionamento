from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QDateEdit
)


class AdicionarCulto(QDialog):

    def __init__(self, obreiros=None, mes=None, ano=None):
        super().__init__()

        self.obreiros = obreiros or []
        self.mes = mes
        self.ano = ano

        self.configurar_janela()
        self.criar_componentes()
        self.criar_layout()
        self.criar_conexoes()

    def configurar_janela(self):
        self.setWindowTitle("Adicionar Culto")
        self.setFixedSize(400, 300)

    def criar_componentes(self):

        # ==========================================
        # Data
        # ==========================================

        self.lbl_data = QLabel("Data do culto")

        self.edit_data = QDateEdit()
        self.edit_data.setCalendarPopup(True)
        self.edit_data.setDisplayFormat("dd/MM/yyyy")

        # Define o mês/ano da escala
        if self.mes and self.ano:

            primeiro_dia = QDate(
                self.ano,
                self.mes,
                1
            )

            ultimo_dia = QDate(
                self.ano,
                self.mes,
                primeiro_dia.daysInMonth()
            )

            self.edit_data.setMinimumDate(primeiro_dia)
            self.edit_data.setMaximumDate(ultimo_dia)
            self.edit_data.setDate(primeiro_dia)

        # ==========================================
        # Nome do culto
        # ==========================================

        self.lbl_culto = QLabel("Nome do culto")

        self.edit_culto = QLineEdit()
        self.edit_culto.setPlaceholderText(
            "Digite o nome do culto"
        )

        # ==========================================
        # Obreiro
        # ==========================================

        self.lbl_obreiro = QLabel("Obreiro")

        self.combo_obreiro = QComboBox()

        self.combo_obreiro.clear()

        self.combo_obreiro.addItem("Selecione...")

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

        layout.addWidget(self.lbl_data)
        layout.addWidget(self.edit_data)

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

        if not culto:

            QMessageBox.warning(
                self,
                "Atenção",
                "Digite o nome do culto."
            )

            return

        if obreiro == "Selecione...":

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione um obreiro."
            )

            return

        self.accept()

    def obter_dados(self):

        data = self.edit_data.date()

        dias_semana = [
            "Segunda",
            "Terça",
            "Quarta",
            "Quinta",
            "Sexta",
            "Sábado",
            "Domingo"
        ]

        dia_semana = dias_semana[
            data.dayOfWeek() - 1
        ]

        return {
            "data": data.toString("dd/MM/yyyy"),
            "dia": dia_semana,
            "culto": self.edit_culto.text().strip(),
            "obreiro": self.combo_obreiro.currentText()
        }