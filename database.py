import sqlite3


class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect("banco/sistema_escalas.db")
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS obreiros(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
        """)

        self.conexao.commit()