class Avaliacao:
    def __init__(self, disciplina, professor, nota_didatica, dificuldade, geral, feedback, id=None):
        self.id = id
        self.disciplina = disciplina
        self.professor = professor
        self.nota_didatica = nota_didatica
        self.dificuldade = dificuldade
        self.geral = geral
        self.feedback = feedback