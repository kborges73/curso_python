from aluno_graduacao import AlunoGraduacao
from aluno_posgraduacao import AlunoPosGraduacao
from curso_enum import Curso    
from linha_pesquisa_enum import LinhaPesquisa

if __name__ == "__main__":
    # Criando um aluno de graduação
    aluno_grad = AlunoGraduacao(matricula="2023001", nome="João Silva", data_nascimento="01/01/2000", curso=Curso.CIENCIA_DA_COMPUTACAO)
    print("Aluno de Graduação:")
    print(aluno_grad)
    print(f"Mensalidade do aluno de graduação: R$ {aluno_grad.calcular_mensalidade():.2f}")

    # Criando um aluno de pós-graduação com bolsa
    aluno_posgrad = AlunoPosGraduacao(matricula="2023002", nome="Maria Oliveira", data_nascimento="15/05/1995", curso=Curso.ENGENHARIA, area_pesquisa=LinhaPesquisa.INOVAÇÃO_TECNOLOGICA, bolsa=50)
    print("Aluno de Pós-Graduação:")
    print(aluno_posgrad)
    print(f"Mensalidade do aluno de pós-graduação com bolsa: R$ {aluno_posgrad.calcular_mensalidade():.2f}")    