from modelo import Avaliacao
from repositorio import AvaliacaoRepository

repo = AvaliacaoRepository()

nova_avaliacao = Avaliacao(
    disciplina="Física Teórica",
    professor="Galina",
    nota_didatica=10.0,
    dificuldade="Fácil",
    geral=9.0,
    feedback="Explica muito bem e resolve questões da lista."
)

repo.salvar(nova_avaliacao)
print("Avaliação salva no banco de dados!")

resultados = repo.buscar_por_professor("Galina")
for r in resultados:
    print(f"Prof: {r.professor} | Disciplina: {r.disciplina} | Didática: {r.nota_didatica} | Geral: {r.geral} | Feedback: {r.feedback}")