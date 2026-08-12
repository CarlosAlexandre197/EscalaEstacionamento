from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4

import os
import sys

def caminho_recurso(nome_arquivo):
    if getattr(sys, "frozen", False):
        pasta = sys._MEIPASS
    else:
        pasta = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(
        pasta,
        "recursos",
        nome_arquivo
    )

def gerar_pdf(nome_arquivo, mes, ano, dados):

    documento = SimpleDocTemplate(
        nome_arquivo,
        pagesize=A4,
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.5 * cm
    )

    estilos = getSampleStyleSheet()

    # ==========================================
    # ESTILOS
    # ==========================================

    nome_igreja = ParagraphStyle(
        "NomeIgreja",
        parent=estilos["Title"],
        fontSize=16,
        leading=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0D4F6F"),
        spaceAfter=5
    )

    titulo = ParagraphStyle(
        "TituloEscala",
        parent=estilos["Title"],
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1565C0"),
        spaceAfter=5
    )

    periodo = ParagraphStyle(
        "Periodo",
        parent=estilos["Heading2"],
        fontSize=13,
        leading=17,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#333333"),
        spaceAfter=15
    )

    rodape = ParagraphStyle(
        "Rodape",
        parent=estilos["Normal"],
        fontSize=8,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#777777")
    )

    elementos = []

    # ==========================================
    # LOGO
    # ==========================================

    caminho_logo = caminho_recurso("logo_igreja.jpg")

    if os.path.exists(caminho_logo):

        logo = Image(
            caminho_logo,
            width=3.5 * cm,
            height=3.5 * cm
        )

        logo.hAlign = "CENTER"

        elementos.append(logo)

        elementos.append(
            Spacer(1, 0.3 * cm)
        )

    # ==========================================
    # NOME DA IGREJA
    # ==========================================

    elementos.append(
        Paragraph(
            "ADSAM 317<br/>"
            "MINISTÉRIO MADUREIRA",
            nome_igreja
        )
    )

    elementos.append(
        Spacer(1, 0.2 * cm)
    )

    # ==========================================
    # TÍTULO
    # ==========================================

    elementos.append(
        Paragraph(
            "ESCALA DO ESTACIONAMENTO",
            titulo
        )
    )

    elementos.append(
        Paragraph(
            f"{mes.upper()} / {ano}",
            periodo
        )
    )

    # ==========================================
    # TABELA
    # ==========================================

    tabela = Table(
        dados,
        colWidths=[
            3.0 * cm,
            3.0 * cm,
            7.5 * cm,
            4.5 * cm
        ],
        repeatRows=1
    )

    estilo_tabela = [

        # --------------------------------------
        # Cabeçalho
        # --------------------------------------

        (
            "BACKGROUND",
            (0, 0),
            (-1, 0),
            colors.HexColor("#0D4F6F")
        ),

        (
            "TEXTCOLOR",
            (0, 0),
            (-1, 0),
            colors.white
        ),

        (
            "FONTNAME",
            (0, 0),
            (-1, 0),
            "Helvetica-Bold"
        ),

        (
            "FONTSIZE",
            (0, 0),
            (-1, 0),
            10
        ),

        # --------------------------------------
        # Corpo
        # --------------------------------------

        (
            "FONTNAME",
            (0, 1),
            (-1, -1),
            "Helvetica"
        ),

        (
            "FONTSIZE",
            (0, 1),
            (-1, -1),
            9
        ),

        # --------------------------------------
        # Alinhamento
        # --------------------------------------

        (
            "ALIGN",
            (0, 0),
            (-1, -1),
            "CENTER"
        ),

        (
            "VALIGN",
            (0, 0),
            (-1, -1),
            "MIDDLE"
        ),

        # --------------------------------------
        # Bordas
        # --------------------------------------

        (
            "GRID",
            (0, 0),
            (-1, -1),
            0.5,
            colors.HexColor("#BDBDBD")
        ),

        # --------------------------------------
        # Espaçamento
        # --------------------------------------

        (
            "TOPPADDING",
            (0, 0),
            (-1, -1),
            8
        ),

        (
            "BOTTOMPADDING",
            (0, 0),
            (-1, -1),
            8
        )
    ]

    # ==========================================
    # LINHAS ALTERNADAS
    # ==========================================

    for linha in range(1, len(dados)):

        if linha % 2 == 0:

            estilo_tabela.append(
                (
                    "BACKGROUND",
                    (0, linha),
                    (-1, linha),
                    colors.HexColor("#F5F7FA")
                )
            )

    tabela.setStyle(
        TableStyle(estilo_tabela)
    )

    elementos.append(tabela)

    # ==========================================
    # ASSINATURA
    # ==========================================

    elementos.append(
        Spacer(1, 1.5 * cm)
    )

    caminho_assinatura = caminho_recurso(
        "assinatura_carlos_alexandre.png"
    )

    if os.path.exists(caminho_assinatura):

        assinatura_img = Image(
            caminho_assinatura,
            width=7 * cm,
            height=3 * cm
        )

        assinatura_img.hAlign = "CENTER"

        elementos.append(
            assinatura_img
        )

        elementos.append(
            Paragraph(
                "Carlos Alexandre<br/>"
                "Responsável pela escala",
                rodape
            )
        )

    else:

        elementos.append(
            Paragraph(
                "________________________________________<br/>"
                "Carlos Alexandre<br/>"
                "Responsável pela escala",
                rodape
            )
        )

    # ==========================================
    # RODAPÉ
    # ==========================================

    elementos.append(
        Spacer(1, 1 * cm)
    )

    elementos.append(
        Paragraph(
            "Escala do Estacionamento",
            rodape
        )
    )

    # ==========================================
    # GERAR PDF
    # ==========================================

    documento.build(elementos)