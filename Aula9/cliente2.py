from validate_docbr import CPF

class Cliente:

    validador_cpf = CPF()
    
    def __init__(self, nome, cpf):
        self.nome= nome
        self.cpf = cpf

    @property
    def nome(self):
        return self._nome
    @property
    def cpf(self):
        return self._cpf
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @cpf.setter
    def cpf(self, novo_cpf):
        if self.validador_cpf.validate(novo_cpf):
            print(f"O CPF {novo_cpf} é válido!")
            self._cpf = novo_cpf
        else:
            print(f"O CPF {novo_cpf} é inválido.")


    def __str__(self):
        return f"Cliente: {self.__nome}, CPF: {self.__cpf}"
    
    def __eq__(self, value):
        if not isinstance(value, Cliente):
            return False
        return self.__cpf == value.__cpf

if __name__ == "__main__":
    cliente1 = Cliente("Maria", "123.456.789-00")
    #print(cliente1.__nome)  # Isso vai gerar um erro, pois __nome é privado
    #print(cliente1.__cpf)   # Isso também vai gerar um erro, pois __cpf
    print(cliente1.get_nome())  # Acessando o nome através do método getter'
    print(cliente1.get_cpf())   # Acessando o CPF através do método getter
    cliente1.set_nome("Maria Silva")  # Alterando o nome através do método setter
    print(cliente1)