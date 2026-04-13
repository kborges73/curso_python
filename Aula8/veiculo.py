class Veiculo:
    """Classe para representar um veículo. """
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def descrever(self):
        """Exibe as informações do veículo. """
        return f"{self.marca} {self.modelo} {self.cor}"
    
    def __eq__(self, value):
        """Compara se dois objetos são iguais. """
        if isinstance(value, Veiculo):
            return self.marca == value.marca and self.modelo == value.modelo and self.cor == value.cor
        return False