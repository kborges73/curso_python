from dataclasses import dataclass, field
from capitulo import Capitulo

@dataclass
class Temporada:
    ano:int 
    quantidade_capitulos: int
    capitulos: list[Capitulo] = field(default_factory=list)
    visto: bool = False

    def adicionar_capitulo(self, capitulo: Capitulo):
        if capitulo not in self.capitulos:
            self.capitulos.append(capitulo)
            print(f"✅ Capítulo '{capitulo.titulo}' adicionado à temporada de {self.ano}")

    def verificar_estado(self):
        if len(self.capitulos) != self.quantidade_capitulos:
            return False
        else:
            for capitulo in self.capitulos:
                if capitulo.visto:
                    visto = True
                else:
                    visto = False
                break       
        return visto