# ============================================
# ESTILO GERAL DO PROGRAMA
# ============================================

JANELA = """
QWidget{
    font-family: Segoe UI;
    font-size: 10pt;
    background-color: #F4F6F9;
}
"""

TITULO = """
QLabel{
    background-color: #1565C0;
    color: white;
    font-size: 20pt;
    font-weight: bold;
    border-radius: 8px;
    padding: 12px;
}
"""

BOTAO_PRIMARIO = """
QPushButton{
    background-color: #1565C0;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 8px;
    font-size: 10pt;
    font-weight: bold;
}

QPushButton:hover{
    background-color: #1976D2;
}

QPushButton:pressed{
    background-color: #0D47A1;
}
"""

BOTAO_SECUNDARIO = """
QPushButton{
    background-color: #43A047;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 8px;
    font-size: 10pt;
    font-weight: bold;
}

QPushButton:hover{
    background-color: #4CAF50;
}
"""

TABELA = """
QTableWidget{
    background: white;
    border:1px solid #C7C7C7;
    gridline-color:#E0E0E0;
    selection-background-color:#BBDEFB;
}

QHeaderView::section{
    background:#1565C0;
    color:white;
    padding:6px;
    font-weight:bold;
    border:none;
}
"""

COMBOBOX = """
QComboBox{
    background:white;
    border:1px solid #BDBDBD;
    border-radius:6px;
    padding:5px;
}
"""

SPINBOX = """
QSpinBox{
    background:white;
    border:1px solid #BDBDBD;
    border-radius:6px;
    padding:5px;
}
"""