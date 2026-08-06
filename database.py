import sqlite3


class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect("banco/sistema_escalas.db")
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    # ==========================================
    # Criação das tabelas
    # ==========================================

    def criar_tabelas(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS obreiros(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
        """)

        self.conexao.commit()

        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS escalas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mes TEXT NOT NULL,
        ano INTEGER NOT NULL,
        dia TEXT NOT NULL,
        culto TEXT NOT NULL,
        obreiro TEXT NOT NULL
    )
""")

self.conexao.commit()

    # ==========================================
    # Obreiros
    # ==========================================

    def salvar_obreiro(self, nome):

        self.cursor.execute(
            "INSERT INTO obreiros(nome) VALUES(?)",
            (nome,)
        )

        self.conexao.commit()

    def listar_obreiros(self):

        self.cursor.execute(
            "SELECT id, nome FROM obreiros ORDER BY nome"
        )

        return self.cursor.fetchall()

    def editar_obreiro(self, id, nome):

        self.cursor.execute(
            "UPDATE obreiros SET nome=? WHERE id=?",
            (nome, id)
        )

        self.conexao.commit()

    def excluir_obreiro(self, id):

        self.cursor.execute(
            "DELETE FROM obreiros WHERE id=?",
            (id,)
        )

        self.conexao.commit()

    # ==========================================
    # Fechar conexão
    # ==========================================

    def salvar_escala(self, mes, ano, dia, culto, obreiro):

    self.cursor.execute("""
        INSERT INTO escalas(
            mes,
            ano,
            dia,
            culto,
            obreiro
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        mes,
        ano,
        dia,
        culto,
        obreiro
    ))

    self.conexao.commit()

    def fechar(self):
        self.conexao.close()