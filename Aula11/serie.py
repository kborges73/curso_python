from temporada import Temporada
from generos import Genero
from dataclasses import dataclass, field

@dataclass
class Serie:
    titulo: str
    imdb_rating:float
    visto: bool = False
    generos: list[Genero] = field(default_factory=list)
    temporadas: list[Temporada] = field(default_factory=list)

    def adicionar_genero(self, genero: Genero):
        if genero not in self.generos:
            self.generos.append(genero)
            print(f"✅ Gênero '{genero.name}' adicionado ao filme '{self.titulo}'")

    def adicionar_temporada(self, temporada: Temporada):
        if temporada not in self.temporadas:
            self.temporadas.append(temporada)
            print(f"✅ Temporada de {temporada.ano} adicionada à série '{self.titulo}'")

    def verificar_estado(self):
        for temporada in self.temporadas:
            if temporada.verificar_estado()==True:
                visto = True
            else:
                visto = False
                break
        return visto
