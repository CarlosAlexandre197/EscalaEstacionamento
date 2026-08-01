from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)


class AdicionarCulto(QDialog):

    def __init__(self):
        super().__init__()

        self.configurar_janela()
        self.criar_componentes()
        self.criar_layout()

    def configurar_janela(self):
        self.setWindowTitle("Adicionar Culto")
        self.setFixedSize(400, 250)

    def criar_componentes(self):

        self.lbl_dia = QLabel("Dia da semana")

        self.combo_dia = QComboBox()
        self.combo_dia.addItems([
            self.combo_dia.addItems([
                "Domingo",
                "Segunda",
                "Terça",
                "Quarta",
                "Quinta",
                "Sexta",
                "Sábado"
            ])
        ])

        self.lbl_culto = QLabel("Nome do culto")

        self.edit_culto = QLineEdit()

        self.lbl_obreiro = QLabel("Obreiro")

        self.combo_obreiro = QComboBox()

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