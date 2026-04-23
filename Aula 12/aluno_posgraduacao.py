from aluno_graduacao import AlunoGraduacao

class AlunoPosGraduacao(AlunoGraduacao):
    def __init__(self, matricula, nome, data_nascimento, area_pesquisa, bolsa=0):
        super().__init__(matricula, nome, data_nascimento)
        self.area_pesquisa = area_pesquisa
        self.bolsa = bolsa

    def __str__(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Data de Nascimento: {self.data_nascimento}, Curso: {self.curso}, Área de Pesquisa: {self.area_pesquisa}"  
    
    def calcular_mensalidade(self):
        valor_desconto = self.area_pesquisa.value * (self.bolsa / 100)
        valor_final = self.area_pesquisa.value - valor_desconto
        return valor_final