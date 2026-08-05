from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)


class CadastroObreiros(QDialog):

    def __init__(self, banco):
        super().__init__()

        self.banco = banco

        self.setWindowTitle("Cadastro de Obreiros")
        self.resize(450, 500)

        self.criar_componentes()
        self.criar_layout()
        self.criar_conexoes()
        self.carregar_obreiros()

    def criar_componentes(self):

        self.lbl_nome = QLabel("Nome do Obreiro:")

        self.txt_nome = QLineEdit()

        self.btn_adicionar = QPushButton("Adicionar")
        self.btn_editar = QPushButton("Editar")
        self.btn_excluir = QPushButton("Excluir")
        self.btn_fechar = QPushButton("Fechar")

        self.lista_obreiros = QListWidget()

    def criar_layout(self):

        layout_principal = QVBoxLayout()

        layout_principal.addWidget(self.lbl_nome)
        layout_principal.addWidget(self.txt_nome)

        layout_botoes = QHBoxLayout()
        layout_botoes.addWidget(self.btn_adicionar)
        layout_botoes.addWidget(self.btn_editar)
        layout_botoes.addWidget(self.btn_excluir)

        layout_principal.addLayout(layout_botoes)

        layout_principal.addWidget(self.lista_obreiros)

        layout_principal.addWidget(self.btn_fechar)

        self.setLayout(layout_principal)

    def criar_conexoes(self):

        self.btn_adicionar.clicked.connect(self.adicionar_obreiro)
        self.btn_editar.clicked.connect(self.editar_obreiro)
        self.btn_excluir.clicked.connect(self.excluir_obreiro)
        self.btn_fechar.clicked.connect(self.close)
        
    def carregar_obreiros(self):

        self.lista_obreiros.clear()

        obreiros = self.banco.listar_obreiros()

        for id_obreiro, nome in obreiros:

            self.lista_obreiros.addItem(nome)

            item = self.lista_obreiros.item(
                self.lista_obreiros.count() - 1
            )

            item.setData(
                256,  # Qt.ItemDataRole.UserRole
                id_obreiro
            )

    def adicionar_obreiro(self):

            nome = self.txt_nome.text().strip()

            if not nome:
                QMessageBox.warning(
                    self,
                    "Atenção",
                    "Digite o nome do obreiro."
                )
                return

            self.lista_obreiros.addItem(nome)
            self.txt_nome.clear()

    def editar_obreiro(self):

        item = self.lista_obreiros.currentItem()

        if item is None:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione um obreiro."
            )
            return

        novo_nome = self.txt_nome.text().strip()

        if not novo_nome:

            QMessageBox.warning(
                self,
                "Atenção",
                "Digite o novo nome."
            )
            return

        id_obreiro = item.data(256)

        try:

            self.banco.editar_obreiro(
                id_obreiro,
                novo_nome
            )

            self.carregar_obreiros()

            self.txt_nome.clear()

        except Exception as erro:

            QMessageBox.warning(
                self,
                "Erro",
                str(erro)
            )

    def excluir_obreiro(self):

        item = self.lista_obreiros.currentItem()

        if item is None:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione um obreiro."
            )
            return

        resposta = QMessageBox.question(
            self,
            "Excluir",
            "Deseja realmente excluir este obreiro?"
        )

        if resposta != QMessageBox.StandardButton.Yes:
            return

        id_obreiro = item.data(256)

        self.banco.excluir_obreiro(id_obreiro)

        self.carregar_obreiros()