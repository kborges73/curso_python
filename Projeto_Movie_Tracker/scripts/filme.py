from dataclasses import dataclass
from dataclasses import field
from operator import attrgetter
from generos_enum import Genero
from video import Video

class Filme(Video):

    def __init__(self, titulo, diretor, ano, imdb_rating=None):  # Corrigido: imdb_ratting -> imdb_rating para consistência
        super().__init__(titulo, imdb_rating)
        self.diretor = diretor
        self.ano = ano

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, value):
        if value < 1895:
            print("O ano de lançamento do filme deve ser maior ou igual a 1895.")
        self._ano = value

    def reproduzir(self):
        print(f"Reproduzindo o filme '{self.titulo}'...")
        self.visto = True

    def __str__(self):
        generos_str = ", ".join([g.name for g in self.lista_generos]) if self.lista_generos else "Nenhum"
        return f"Filme: {self.titulo} | Diretor: {self.diretor} | Ano: {self.ano} | IMDb: {self.imdb_rating} | Gêneros: {generos_str}"

#---------------Teste---------------
if __name__ == "__main__":            
    filme1 = Filme("O Poderoso Chefão", "Francis Ford Coppola", 1972, 9.2)
    filme1.adicionar_genero(Genero.POLICIAL)
    print(filme1)
    print(f"Estado antes de reproduzir: {'Visto' if filme1.visto else 'Não visto'}")
    filme1.reproduzir()
    print(f"Estado depois de reproduzir: {'Visto' if filme1.visto else 'Não visto'}")
    
    filme2 = Filme("Cidadão Kane", "Orson Welles", 1800, 8.3)
    filme2.adicionar_genero(Genero.DRAMA)
    filme2.adicionar_genero(Genero.POLICIAL)
    print(filme2)
    filme2.reproduzir()

    filme3 = Filme("O Mágico de Oz", "Victor Fleming", 1939, 7.3)
    filme3.adicionar_genero(Genero.AVENTURA)
    filme3.adicionar_genero(Genero.FICCAO_CIENTIFICA)
    filme3.adicionar_genero(Genero.MUSICAL)
    print(filme3)
    filme3.reproduzir()

    lista_filmes = [filme1, filme2, filme3]
    lista_filmes.sort(key=attrgetter("imdb_rating"))  
    print("Filmes ordenados por IMDb:")
    for filme in lista_filmes:
        print(f"{filme.titulo}: {filme.imdb_rating}")