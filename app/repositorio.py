import sqlite3
from modelo import Avaliacao

class AvaliacaoRepository:
    def __init__(self, db_name="avaliacoes.db"):
        self.db_name = db_name
        self.criar_tabela()

    def conectar(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row 
        return conn

    def criar_tabela(self):
        query = '''
        CREATE TABLE IF NOT EXISTS avaliacao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            disciplina TEXT NOT NULL,
            professor TEXT NOT NULL,
            nota_didatica REAL,
            dificuldade TEXT,
            geral REAL,
            feedback TEXT
        )
        '''
        with self.conectar() as conn:
            conn.execute(query)

    def salvar(self, avaliacao):
        query = '''
        INSERT INTO avaliacao (disciplina, professor, nota_didatica, dificuldade, geral, feedback)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        with self.conectar() as conn:
            cursor = conn.execute(query, (
                avaliacao.disciplina, avaliacao.professor, 
                avaliacao.nota_didatica, avaliacao.dificuldade, avaliacao.geral, avaliacao.feedback,
            ))
            avaliacao.id = cursor.lastrowid
        return avaliacao

    def buscar_por_professor(self, nome_professor):
        query = 'SELECT * FROM avaliacao WHERE professor LIKE ?'
        with self.conectar() as conn:
            cursor = conn.execute(query, ('%' + nome_professor + '%',))
            linhas = cursor.fetchall()
        return [Avaliacao(**dict(linha)) for linha in linhas]