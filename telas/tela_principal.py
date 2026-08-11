from whatsapp import abrir_whatsapp
from gerar_pdf import gerar_pdf
from datas import obter_datas
from telas.cadastro_obreiros import CadastroObreiros

from style import (
    JANELA,
    TITULO,
    GROUPBOX,
    BOTAO_PRIMARIO,
    BOTAO_SECUNDARIO,
    TABELA,
    COMBOBOX,
    SPINBOX
)

from telas.adicionar_culto import AdicionarCulto
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QDialog,
    QLabel,
    QPushButton,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QSpinBox,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QMessageBox,
    QFileDialog
)


class TelaPrincipal(QWidget):

    def __init__(self, banco):
        super().__init__()
        
        self.banco = banco

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
        self.btn_whatsapp = QPushButton("📱 WhatsApp")
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
            botao.setMinimumHeight(4)

        # ==========================================
        # Tabela
        # ==========================================

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(4)

        self.tabela.setHorizontalHeaderLabels([
            "Data",
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

        # Cultos fixos
        cultos = [
            ("Domingo", "Escola Bíblica"),
            ("Domingo", "Culto da Família"),
            ("Quarta", "Culto de Doutrina e Causas Impossíveis")
        ]

        # Pega o mês selecionado no QComboBox
        mes = self.combo_mes.currentIndex() + 1

        # Pega o ano selecionado
        ano = self.spin_ano.value()

        # Busca os obreiros cadastrados
        obreiros = self.obter_nomes_obreiros()

        # Limpa a tabela
        self.tabela.setRowCount(0)

        linhas = []

        # Gera todas as datas dos cultos
        for dia_semana, culto in cultos:

            datas = obter_datas(
                dia_semana,
                mes,
                ano
            )

            for data in datas:

                linhas.append(
                    (data, dia_semana, culto)
                )

        # Ordena pela data
        linhas.sort(
            key=lambda linha: (
                int(linha[0][6:10]),
                int(linha[0][3:5]),
                int(linha[0][0:2])
            )
        )

        # Preenche a tabela
        for data, dia_semana, culto in linhas:

            linha = self.tabela.rowCount()

            self.tabela.insertRow(linha)

            self.tabela.setItem(
                linha,
                0,
                QTableWidgetItem(data)
            )

            self.tabela.setItem(
                linha,
                1,
                QTableWidgetItem(dia_semana)
            )

            self.tabela.setItem(
                linha,
                2,
                QTableWidgetItem(culto)
            )

            # ComboBox dos obreiros
            combo_obreiro = QComboBox()

            combo_obreiro.addItem("Selecione...")

            for nome in obreiros:
                combo_obreiro.addItem(nome)

            self.tabela.setCellWidget(
                linha,
                3,
                combo_obreiro
            )

        self.carregar_escala()
            
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
layout_botoes.addWidget(self.btn_whatsapp)

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
        
        self.grupo_dados.setStyleSheet(GROUPBOX)
        self.grupo_escala.setStyleSheet(GROUPBOX)
        
    def criar_conexoes(self):

        self.btn_adicionar.clicked.connect(self.adicionar_culto)
        self.btn_remover.clicked.connect(self.remover_culto)

        self.btn_obreiros.clicked.connect(self.abrir_cadastro_obreiros)
        
        self.btn_salvar.clicked.connect(self.salvar_escala)

        self.btn_pdf.clicked.connect(self.gerar_pdf_escala)


self.btn_whatsapp.clicked.connect(self.enviar_whatsapp)

        self.combo_mes.currentIndexChanged.connect(
            self.preencher_tabela
        )

        self.spin_ano.valueChanged.connect(
            self.preencher_tabela
        )
        
    def adicionar_culto(self):

        obreiros = self.obter_nomes_obreiros()

        mes = self.combo_mes.currentIndex() + 1
        ano = self.spin_ano.value()

        janela = AdicionarCulto(
            obreiros,
            mes,
            ano
        )

        if janela.exec() == QDialog.DialogCode.Accepted:

            dados = janela.obter_dados()

            print("Novo culto:", dados)

            # Adiciona na tabela
            self.adicionar_culto_tabela(
                dados["data"],
                dados["dia"],
                dados["culto"],
                dados["obreiro"]
            )

            # Salva no banco
            self.banco.salvar_escala(
                self.combo_mes.currentText(),
                ano,
                dados["data"],
                dados["dia"],
                dados["culto"],
                dados["obreiro"]
            )

            QMessageBox.information(
                self,
                "Sucesso",
                "Culto adicionado e salvo com sucesso!"
            )

    
    def remover_culto(self):

        linha = self.tabela.currentRow()

        # Nenhuma linha selecionada
        if linha < 0:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione um culto na tabela para remover."
            )

            return

        # ==========================================
        # Dados da linha selecionada
        # ==========================================

        data = self.tabela.item(
            linha,
            0
        ).text()

        culto = self.tabela.item(
            linha,
            2
        ).text()

        # ==========================================
        # Cultos fixos
        # ==========================================

        cultos_fixos = [
            "Escola Bíblica",
            "Culto da Família",
            "Culto de Doutrina e Causas Impossíveis"
        ]

        if culto in cultos_fixos:

            QMessageBox.information(
                self,
                "Culto fixo",
                "Esse culto é fixo e não pode ser removido."
            )

            return

        # ==========================================
        # Confirmação
        # ==========================================

        resposta = QMessageBox.question(
            self,
            "Confirmar remoção",
            f"Deseja remover o culto?\n\n"
            f"Data: {data}\n"
            f"Culto: {culto}",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if resposta != QMessageBox.StandardButton.Yes:
            return

        # ==========================================
        # Remove do banco
        # ==========================================

        mes = self.combo_mes.currentText()
        ano = self.spin_ano.value()

        self.banco.excluir_escala(
            mes,
            ano,
            data,
            culto
        )

        # ==========================================
        # Remove da tabela
        # ==========================================

        self.tabela.removeRow(linha)

        QMessageBox.information(
            self,
            "Sucesso",
            "Culto removido com sucesso!"
        )

    def abrir_cadastro_obreiros(self):

        janela = CadastroObreiros(self.banco)
        janela.exec()
        
    def obter_nomes_obreiros(self):

        obreiros = self.banco.listar_obreiros()

        print("OBREIROS VINDOS DO BANCO:")
        print(obreiros)

        return [
            nome
            for _, nome in obreiros
            if nome and nome.strip().lower() != "selecione..."
        ]
    
    def salvar_escala(self):

        mes = self.combo_mes.currentText()
        ano = self.spin_ano.value()

        cultos_sem_obreiro = []

        # ==========================================
        # Primeiro verifica se existe algum culto
        # sem obreiro
        # ==========================================

        for linha in range(self.tabela.rowCount()):

            data = self.tabela.item(linha, 0).text()
            culto = self.tabela.item(linha, 2).text()

            combo = self.tabela.cellWidget(linha, 3)

            if combo is None:
                continue

            obreiro = combo.currentText()

            if obreiro == "Selecione...":
                cultos_sem_obreiro.append(
                    f"{data} — {culto}"
                )

        # ==========================================
        # Se encontrou cultos sem obreiro
        # ==========================================

        if cultos_sem_obreiro:

            lista = "\n".join(
                cultos_sem_obreiro
            )

            QMessageBox.warning(
                self,
                "Escala incompleta",
                "Os seguintes cultos estão sem obreiro:\n\n"
                + lista
                + "\n\n"
                "Selecione um obreiro antes de salvar."
            )

            return

        # ==========================================
        # Todos possuem obreiro
        # ==========================================

        for linha in range(self.tabela.rowCount()):

            data = self.tabela.item(
                linha,
                0
            ).text()

            dia = self.tabela.item(
                linha,
                1
            ).text()

            culto = self.tabela.item(
                linha,
                2
            ).text()

            combo = self.tabela.cellWidget(
                linha,
                3
            )

            if combo is None:
                continue

            obreiro = combo.currentText()

            self.banco.salvar_escala(
                mes,
                ano,
                data,
                dia,
                culto,
                obreiro
            )

        QMessageBox.information(
            self,
            "Sucesso",
            "Escala salva com sucesso!"
        )

    def carregar_escala(self):

        mes = self.combo_mes.currentText()
        ano = self.spin_ano.value()

        escala = self.banco.listar_escala(
            mes,
            ano
        )

        if not escala:
            return

        for data_bd, dia_bd, culto_bd, obreiro_bd in escala:

            encontrou = False

            # Procura se a linha já existe
            for linha in range(self.tabela.rowCount()):

                data = self.tabela.item(
                    linha,
                    0
                ).text()

                culto = self.tabela.item(
                    linha,
                    2
                ).text()

                if data == data_bd and culto == culto_bd:

                    combo = self.tabela.cellWidget(
                        linha,
                        3
                    )

                    if combo is not None:

                        indice = combo.findText(
                            obreiro_bd
                        )

                        if indice >= 0:
                            combo.setCurrentIndex(indice)

                    encontrou = True
                    break

            # ==========================================
            # Se não encontrou, é um culto personalizado
            # ==========================================

            if not encontrou:

                self.adicionar_culto_tabela(
                    data_bd,
                    dia_bd,
                    culto_bd,
                    obreiro_bd
                )

    def gerar_pdf_escala(self):

        mes = self.combo_mes.currentText()
        ano = self.spin_ano.value()

        arquivo, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar PDF",
            f"Escala_{mes}_{ano}.pdf",
            "Arquivos PDF (*.pdf)"
        )

        if not arquivo:
            return

        dados = [
            ["Data", "Dia", "Culto", "Obreiro"]
        ]

        for linha in range(self.tabela.rowCount()):

            data = self.tabela.item(linha, 0).text()
            dia = self.tabela.item(linha, 1).text()
            culto = self.tabela.item(linha, 2).text()

            combo = self.tabela.cellWidget(linha, 3)

            if combo is not None:
                obreiro = combo.currentText()
            else:
                obreiro = ""

            dados.append([
                data,
                dia,
                culto,
                obreiro
            ])

        try:

            gerar_pdf(
                arquivo,
                mes,
                ano,
                dados
            )

            QMessageBox.information(
                self,
                "Sucesso",
                f"PDF gerado com sucesso!\n\n{arquivo}"
            )

        except Exception as erro:

            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível gerar o PDF:\n\n{erro}"
            )
            
    def adicionar_culto_tabela(
        self,
        data,
        dia_semana,
        culto,
        obreiro
        ):

        # ==========================================
        # Verifica se o culto já existe na tabela
        # ==========================================

        for linha in range(self.tabela.rowCount()):

            data_existente = self.tabela.item(
                linha,
                0
            ).text()

            culto_existente = self.tabela.item(
                linha,
                2
            ).text()

            if (
                data_existente == data
                and culto_existente == culto
            ):

                QMessageBox.warning(
                    self,
                    "Atenção",
                    "Esse culto já está cadastrado nessa data."
                )

                return

        # ==========================================
        # Adiciona somente UMA linha
        # ==========================================

        linha = self.tabela.rowCount()

        self.tabela.insertRow(linha)

        self.tabela.setItem(
            linha,
            0,
            QTableWidgetItem(data)
        )

        self.tabela.setItem(
            linha,
            1,
            QTableWidgetItem(dia_semana)
        )

        self.tabela.setItem(
            linha,
            2,
            QTableWidgetItem(culto)
        )

        # ==========================================
        # ComboBox de obreiro
        # ==========================================

        combo_obreiro = QComboBox()

        combo_obreiro.addItem("Selecione...")

        for nome in self.obter_nomes_obreiros():

            if nome != "Selecione...":
                combo_obreiro.addItem(nome)

        indice = combo_obreiro.findText(obreiro)

        if indice >= 0:
            combo_obreiro.setCurrentIndex(indice)

        self.tabela.setCellWidget(
            linha,
            3,
            combo_obreiro
        )

        self.ordenar_tabela_por_data()

    def ordenar_tabela_por_data(self):

        self.tabela.sortItems(
            0,
            Qt.SortOrder.AscendingOrder
        )
        
