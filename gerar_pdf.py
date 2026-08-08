from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm


def gerar_pdf(nome_arquivo, mes, ano, dados):

    documento = SimpleDocTemplate(
        nome_arquivo,
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm
    )

    estilos = getSampleStyleSheet()

    titulo = ParagraphStyle(
        "TituloEscala",
        parent=estilos["Title"],
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1565C0"),
        spaceAfter=8
    )

    periodo = ParagraphStyle(
        "Periodo",
        parent=estilos["Heading2"],
        fontSize=14,
        leading=18,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#333333"),
        spaceAfter=20
    )

    elementos = []

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

    tabela = Table(
        dados,
        colWidths=[
            3.0 * cm,
            3.0 * cm,
            8.0 * cm,
            4.0 * cm
        ],
        repeatRows=1
    )

    estilo_tabela = [
        # Cabeçalho
        (
            "BACKGROUND",
            (0, 0),
            (-1, 0),
            colors.HexColor("#1565C0")
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

        # Corpo
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

        # Alinhamento
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

        # Bordas
        (
            "GRID",
            (0, 0),
            (-1, -1),
            0.5,
            colors.HexColor("#BDBDBD")
        ),

        # Espaçamento
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

    # Linhas alternadas
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

    elementos.append(
        Spacer(1, 2 * cm)
    )

    assinatura = Table(
        [
            ["________________________________________"],
            ["Responsável pela escala"]
        ],
        colWidths=[7 * cm]
    )

    assinatura.setStyle(
        TableStyle([
            (
                "ALIGN",
                (0, 0),
                (-1, -1),
                "CENTER"
            ),
            (
                "FONTNAME",
                (0, 1),
                (-1, 1),
                "Helvetica"
            ),
            (
                "FONTSIZE",
                (0, 1),
                (-1, 1),
                9
            )
        ])
    )

    elementos.append(assinatura)

    documento.build(elementos)