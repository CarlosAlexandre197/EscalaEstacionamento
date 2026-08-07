from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
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

    elementos = []

    titulo = Paragraph(
        "<b>ESCALA DO ESTACIONAMENTO</b>",
        estilos["Title"]
    )

    elementos.append(titulo)

    elementos.append(
        Paragraph(
            f"<b>{mes} / {ano}</b>",
            estilos["Heading2"]
        )
    )

    tabela = Table(dados)

    tabela.setStyle(TableStyle([

        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1565C0")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("GRID", (0, 0), (-1, -1), 1, colors.grey),

        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 10)

    ]))

    elementos.append(tabela)

    documento.build(elementos)