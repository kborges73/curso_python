class Cliente:
    def __init__(self, nome, idade, cpf):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("Idade não pode ser negativa")
        self._idade = valor

#--------------TESTE-----------------
if __name__ == "__main__":
    try:
        cliente1 = Cliente("Maria", 15, "123.456.789-00")
        print(cliente1.idade)
    except ValueError as e:
        print(e)  # Saída: Idade não pode ser negativa
    else:
        print("Cliente criado com sucesso!")
    finally:
        print("Teste concluído.")