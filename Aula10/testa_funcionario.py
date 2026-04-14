from funcionario import Funcionario
from meses import Mes

class TestaFuncionario:
    funcionario = Funcionario ('Matheus', 'matheus@blablabla.com.br', 50)
    funcionario.registrar_horas(Mes.JANEIRO, 300)
    funcionario.registrar_horas(Mes.FEVEREIRO, 200)
    salario = funcionario.calcular_salario(Mes.JANEIRO)
    print(funcionario)
    print(f"Salário de Jan: R${salario:.2f}")
    print(funcionario.emitir_relatorio())   
