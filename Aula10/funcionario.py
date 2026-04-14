from meses import Mes

class Funcionario:
    def __init__(self, nome, email, valor_hora):
        self.nome = nome
        self.email = email
        self.valor_hora = valor_hora
        self.horas: dict [Mes, int] = {} #mes e horas trabalhadas

    def registrar_horas(self, mes: Mes, horas_trabalhadas):
        self.horas[mes] = horas_trabalhadas

    def calcular_salario(self, mes: Mes):
        if mes in self.horas:
            return self.horas[mes] * self.valor_hora
        else:
            return 0        
        
    def emitir_relatorio(self):
        relatorio = f"Relatório de Horas para {self.nome}:\n"
        for mes, horas in self.horas.items():
            salario = self.calcular_salario(mes)
            relatorio += f"Mês: {mes.name}, Horas Trabalhadas: {horas}, Salário: R${salario:.2f}\n"
        return relatorio

    def __str__(self):
        return f"Funcionario: {self.nome}, Email: {self.email}, Valor Hora: {self.valor_hora}"