# ==========================================
# JANELA
# ==========================================

JANELA = """
QWidget {
    background-color: #F4F6F9;
    color: #222222;
    font-family: Segoe UI;
    font-size: 11pt;
}

QLabel {
    color: #222222;
    background: transparent;
}
"""
# ==========================================
# TÍTULO
# ==========================================

TITULO = """
QLabel {
    background-color: #1565C0;
    color: white;
    font-size: 24px;
    font-weight: bold;
    border-radius: 8px;
    padding: 12px;
}
"""

# ==========================================
# GROUPBOX
# ==========================================

GROUPBOX = """
QGroupBox {
    color: #1565C0;
    font-size: 14px;
    font-weight: bold;
    border: 2px solid #D0D0D0;
    border-radius: 8px;
    margin-top: 15px;
    padding-top: 18px;
    background-color: white;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 15px;
    padding: 0 6px;
    color: #1565C0;
    background-color: white;
}
"""

# ==========================================
# BOTÃO PRIMÁRIO
# ==========================================

BOTAO_PRIMARIO = """
QPushButton {
    background-color: #1565C0;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 8px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #1976D2;
}

QPushButton:pressed {
    background-color: #0D47A1;
}
"""

# ==========================================
# BOTÃO SECUNDÁRIO
# ==========================================

BOTAO_SECUNDARIO = """
QPushButton {
    background-color: #43A047;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 8px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #4CAF50;
}

QPushButton:pressed {
    background-color: #2E7D32;
}
"""

BOTAO_WHATSAPP = """
QPushButton {
    background-color: #25D366;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #20BD5A;
}

QPushButton:pressed {
    background-color: #1DA851;
}
"""

# ==========================================
# COMBOBOX
# ==========================================

COMBOBOX = """
QComboBox {
    background-color: white;
    border: 1px solid #BDBDBD;
    border-radius: 5px;
    padding: 6px;
    padding-right: 25px;
}

QComboBox::drop-down {
    width: 22px;
    border-left: 1px solid #BDBDBD;
    background-color: #E8E8E8;
}

QComboBox::drop-down:hover {
    background-color: #D0D0D0;
}
"""

# ==========================================
# SPINBOX
# ==========================================

SPINBOX = """
QSpinBox {
    background-color: white;
    border: 1px solid #BDBDBD;
    border-radius: 5px;
    padding: 6px;
    padding-right: 25px;
}

QSpinBox::up-button {
    subcontrol-origin: border;
    subcontrol-position: top right;
    width: 20px;
    height: 14px;
    background-color: #E8E8E8;
    border-left: 1px solid #BDBDBD;
}

QSpinBox::down-button {
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width: 20px;
    height: 14px;
    background-color: #E8E8E8;
    border-left: 1px solid #BDBDBD;
}

QSpinBox::up-button:hover,
QSpinBox::down-button:hover {
    background-color: #D0D0D0;
}
"""

# ==========================================
# TABELA
# ==========================================

TABELA = """
QTableWidget {
    background-color: white;
    color: #222222;
    alternate-background-color: #F7F7F7;
    border: 1px solid #D0D0D0;
    gridline-color: #E0E0E0;
    selection-background-color: #BBDEFB;
}

QTableWidget::item {
    color: #222222;
}

QHeaderView::section {
    background-color: #1565C0;
    color: white;
    padding: 8px;
    border: none;
    font-weight: bold;
}
"""