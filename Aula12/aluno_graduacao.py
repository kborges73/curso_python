class AlunoGraduacao:
    def __init__(self, matricula, nome, data_nascimento, curso):
        self.matricula = matricula
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.curso = curso

    def __str__(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Data de Nascimento: {self.data_nascimento}, Curso: {self.curso}",

    def calcular_mensalidade(self):
        return self.curso.value