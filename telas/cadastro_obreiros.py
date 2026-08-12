from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
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
        self.btn_atualizar = QPushButton("🔄 Atualizar")
        self.btn_fechar = QPushButton("Fechar")

        self.tabela_obreiros = QTableWidget()

        self.tabela_obreiros.setColumnCount(2)

        self.tabela_obreiros.setHorizontalHeaderLabels([
            "ID",
            "Nome"
        ])

        self.tabela_obreiros.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.tabela_obreiros.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.tabela_obreiros.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        self.tabela_obreiros.verticalHeader().setVisible(False)

        self.tabela_obreiros.setAlternatingRowColors(True)

        self.tabela_obreiros.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.tabela_obreiros.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )

        self.tabela_obreiros.setColumnWidth(0, 70)

    def criar_layout(self):

        layout_principal = QVBoxLayout()

        layout_principal.addWidget(self.lbl_nome)
        layout_principal.addWidget(self.txt_nome)

        layout_botoes = QHBoxLayout()
        layout_botoes.addWidget(self.btn_adicionar)
        layout_botoes.addWidget(self.btn_editar)
        layout_botoes.addWidget(self.btn_excluir)
        layout_botoes.addWidget(self.btn_atualizar)

        layout_principal.addLayout(layout_botoes)

        layout_principal.addWidget(self.tabela_obreiros)

        layout_principal.addWidget(self.btn_fechar)

        self.setLayout(layout_principal)

    def criar_conexoes(self):

        self.btn_adicionar.clicked.connect(self.adicionar_obreiro)
        self.btn_editar.clicked.connect(self.editar_obreiro)
        self.btn_excluir.clicked.connect(self.excluir_obreiro)
        self.btn_fechar.clicked.connect(self.close)

        self.tabela_obreiros.itemSelectionChanged.connect(
            self.selecionar_obreiro
        )
        
    def carregar_obreiros(self):

        self.tabela_obreiros.setRowCount(0)

        obreiros = self.banco.listar_obreiros()

        for linha, (id_obreiro, nome) in enumerate(obreiros):

            self.tabela_obreiros.insertRow(linha)

            self.tabela_obreiros.setItem(
                linha,
                0,
                QTableWidgetItem(str(id_obreiro))
            )

            self.tabela_obreiros.setItem(
                linha,
                1,
                QTableWidgetItem(nome)
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

        try:

            self.banco.salvar_obreiro(nome)

            self.carregar_obreiros()

            self.txt_nome.clear()

        except Exception as erro:

            QMessageBox.warning(
                self,
                "Erro",
                f"Não foi possível cadastrar o obreiro:\n\n{erro}"
            )

    def editar_obreiro(self):

        linha = self.tabela_obreiros.currentRow()

        if linha < 0:

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

        id_obreiro = int(
            self.tabela_obreiros.item(linha, 0).text()
        )

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

        linha = self.tabela_obreiros.currentRow()

        if linha < 0:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione um obreiro."
            )
            return

        id_obreiro = int(
            self.tabela_obreiros.item(linha, 0).text()
        )

        resposta = QMessageBox.question(
            self,
            "Confirmação",
            "Deseja realmente excluir este obreiro?"
        )

        if resposta == QMessageBox.StandardButton.Yes:

            self.banco.excluir_obreiro(id_obreiro)

            self.carregar_obreiros()
            self.txt_nome.clear()

    def selecionar_obreiro(self):

        linha = self.tabela_obreiros.currentRow()

        if linha >= 0:

            nome = self.tabela_obreiros.item(
                linha,
                1
            ).text()

            self.txt_nome.setText(nome)