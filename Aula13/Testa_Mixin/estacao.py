class Estacao:
    def __init__(self, nome, frequencia, fm=True):
        self.nome = nome
        self.frequencia = frequencia
        self.fm = fm

    def __str__(self):
        return f"{self.nome} ({self.frequencia} MHz)"