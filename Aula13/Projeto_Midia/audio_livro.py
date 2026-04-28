from livro import Livro
from narrador import Narrador

class Audio_Livro(Livro):
    def __init__(self, titulo, ano, autor, isbn, narrador, tempoLeitura):
        super().__init__(titulo, ano, autor, isbn)
        self.narrador = narrador
        self.tempoLeitura = tempoLeitura

    def reproduzir(self, velocidade=1.0):
        return f"O narrador {self.narrador.nome} está lendo o livro '{self.titulo}' de {self.autor} ({self.ano}) - Editora: {self.editora.nome} - Velocidade de leitura: {velocidade:.2f}x"