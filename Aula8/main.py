from veiculo import Veiculo

if __name__ == "__main__":
    # Criando um objeto Veiculo
    meu_veiculo = Veiculo("Toyota", "Corolla", "Branco")

    # Exibindo as informações do veículo
    print("Dados do meu veiculo")
    print(meu_veiculo.descrever())
    print(id(meu_veiculo))  # Exibe o ID do objeto

    meu_veiculo2 = Veiculo("Toyota", "Corolla", "Branco")
    print("Dados do meu veiculo 2")
    print(meu_veiculo2.descrever())
    print(id(meu_veiculo2))  # Exibe o ID do objeto

    teste = meu_veiculo is meu_veiculo2
    print("Veiculo1 é o veiculo2? " + str(teste))  # Exibe se os objetos são o mesmo (True ou False

    meu_veiculo3 = meu_veiculo
    print("Dados do meu veiculo 3")
    print(meu_veiculo3.descrever())
    print(id(meu_veiculo3))  # Exibe o ID do objeto
    print("Veiculo1 e 3 são iguais? " + str(meu_veiculo == meu_veiculo3))