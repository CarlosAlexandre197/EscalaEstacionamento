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

        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS escalas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mes TEXT NOT NULL,
                ano INTEGER NOT NULL,
                data TEXT NOT NULL,
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

    def salvar_escala(self, mes, ano, data, dia, culto, obreiro):

        # Verifica se essa escala já existe
        self.cursor.execute("""
            SELECT id
            FROM escalas
            WHERE mes = ?
            AND ano = ?
            AND data = ?
            AND culto = ?
        """, (
            mes,
            ano,
            data,
            culto
        ))

        registro = self.cursor.fetchone()

        if registro:

            # Atualiza o obreiro existente
            self.cursor.execute("""
                UPDATE escalas
                SET dia = ?,
                    obreiro = ?
                WHERE id = ?
            """, (
                dia,
                obreiro,
                registro[0]
            ))

        else:

            # Cria uma nova escala
            self.cursor.execute("""
                INSERT INTO escalas(
                    mes,
                    ano,
                    data,
                    dia,
                    culto,
                    obreiro
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                mes,
                ano,
                data,
                dia,
                culto,
                obreiro
            ))

        self.conexao.commit()

    def listar_escala(self, mes, ano):

        self.cursor.execute("""
            SELECT
                data,
                dia,
                culto,
                obreiro
            FROM escalas
            WHERE mes = ?
            AND ano = ?
            ORDER BY data
        """, (mes, ano))

        return self.cursor.fetchall()
    
    def limpar_escalas(self):

        self.cursor.execute("DELETE FROM escalas")

        self.conexao.commit()

    def excluir_escala(self, mes, ano, data, culto):

        self.cursor.execute("""
            DELETE FROM escalas
            WHERE mes = ?
            AND ano = ?
            AND data = ?
            AND culto = ?
        """, (
            mes,
            ano,
            data,
            culto
        ))

        self.conexao.commit()

    def fechar(self):
        self.conexao.close()