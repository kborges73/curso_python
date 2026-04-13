class Cliente:
    
    def __init__(self, nome, cpf):
        self.__nome= nome
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

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