from dataclasses import dataclass
from dataclasses import field
from operator import attrgetter
from generos import Genero

@dataclass
class Filme:
    titulo: str
    diretor: str
    ano: int
    imdb_rating:float
    visto: bool = False
    generos: list[Genero] = field(default_factory=list)

    def __post_init__(self):
        if self.ano < 1895:
            print("O ano de lançamento do filme deve ser maior ou igual a 1895.")

    def adicionar_genero(self, genero: Genero):
        if genero not in self.generos:
            self.generos.append(genero)
            print(f"✅ Gênero '{genero.name}' adicionado ao filme '{self.titulo}'")

#---------------Teste---------------
if __name__ == "__main__":            
    filme1 = Filme("O Poderoso Chefão", "Francis Ford Coppola", 1972, 9.2)
    filme1.adicionar_genero(Genero.POLICIAL)
    print(filme1)
    
    filme2 = Filme("Cidadão Kane", "Orson Welles", 1800, 8.3)
    filme2.adicionar_genero(Genero.DRAMA)
    filme2.adicionar_genero(Genero.POLICIAL)
    print(filme2)

    filme3= Filme("O Mágico de Oz", "Victor Fleming", 1939, 7.3)
    filme3.adicionar_genero(Genero.AVENTURA)
    filme3.adicionar_genero(Genero.FICCAO_CIENTIFICA)
    filme3.adicionar_genero(Genero.MUSICAL)
    print(filme3)

    lista_filmes = [filme1, filme2, filme3]
    lista_filmes.sort(key=attrgetter("imdb_rating"))   

    for filme in lista_filmes:
        print(f"{filme.titulo} - IMDb Rating: {filme.imdb_rating}") 

    lista_filmes.sort(key=attrgetter("imdb_rating"), reverse=True) 

    for filme in lista_filmes:
        print(f"{filme.titulo} - IMDb Rating: {filme.imdb_rating}") 