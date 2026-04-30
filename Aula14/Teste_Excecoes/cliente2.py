from validate_docbr import CPF  
from campo_faltante_excepption import CampoFaltanteException

class Cliente:
    validador_cpf = CPF()

    def __init__(self, nome, idade, cpf):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome
    
    

    @property
    def idade(self):       
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        else:
            self._idade = idade

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if self.validador_cpf.validate(cpf):
            self._cpf = cpf #usa o _ para evitar recursão infinita
        else:
            raise ValueError(f"O CPF {cpf} é inválido.")
    
    # Equivalente direto ao toString() para o utilizador
    def __str__(self):
        return f" {self.nome} possui o cpf {self.cpf}."
    
    @nome.setter
    def nome(self, nome):
        if not nome: #Em Python, strings vazias ("") são avaliadas como False, 
            #enquanto qualquer string com pelo menos um caractere é avaliada como True. 
            raise CampoFaltanteException("campo obrigatório não informado", "nome")
        else:
            self._nome = nome

#--------------TESTE-----------------
if __name__ == "__main__":
    try:
        cliente1 = Cliente("", -15,"987.654.321-00")
        #cliente1 = Cliente("Maria", 25, "123.456.789-00")
        print(str(cliente1))  # Deve usar o __str__
    except CampoFaltanteException as e:
        print(e)  # Saída: campo obrigatório não informado
        print(f"Erro no campo: {e.nome_campo}")  # Saída: Erro no campo: nome


    # except Exception as e:
    #     print(f"Ocorreu um erro inesperado: {e}")
    # else: 
    #     print("Cliente criado com sucesso.")






    # finally:
    #     print("Teste concluído.")

