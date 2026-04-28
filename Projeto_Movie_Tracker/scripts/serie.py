from temporada import Temporada
from generos_enum import Genero
from video import Video
from capitulo import Capitulo
from datetime import datetime

class Serie(Video):
    def __init__(self, titulo, imdb_rating=None):
        super().__init__(titulo, imdb_rating)
        self.temporadas = []

    def adicionar_temporada(self, temporada: Temporada):
        if temporada not in self.temporadas:
            self.temporadas.append(temporada)
            print(f"✅ Temporada de {temporada.ano} adicionada à série '{self.titulo}'")

    #Sobrescrita de verificar_estado para considerar as temporadas
    def verificar_estado(self):
        for temporada in self.temporadas:
            if temporada.verificar_estado()==True:
                self.visto = True
            else:
                self.visto = False
                break
        return self.visto

    def reproduzir(self):
        print(f"Reproduzindo a série '{self.titulo}'...")
        for temporada in self.temporadas:
            for capitulo in temporada.capitulos:
                if not capitulo.visto:
                    print(f"Reproduzindo o capítulo '{capitulo.titulo}' da temporada de {temporada.ano}...")
                    capitulo.visto = True
        self.visto = True

    def reproduzir_temporada(self, nro_temporada):
        temporada = self.temporadas[nro_temporada-1]  # Ajuste para índice baseado em 0
        print(f"Reproduzindo a temporada de {temporada.ano} da série '{self.titulo}'...")
        for capitulo in temporada.capitulos:
            if not capitulo.visto:
                print(f"Reproduzindo o capítulo '{capitulo.titulo}' da temporada de {temporada.ano}...")
                capitulo.visto = True

#---------------Teste---------------
if __name__ == "__main__":  
    serie1 = Serie(titulo="Breaking Bad", 
                    imdb_rating=9.5, 
                )
    serie1.adicionar_genero(Genero.DRAMA)
    serie1.adicionar_genero(Genero.POLICIAL)    

    serie1.adicionar_temporada(Temporada(ano=2008, quantidade_capitulos=5))
    serie1.adicionar_temporada(Temporada(ano=2009, quantidade_capitulos=5))
        
    temporada1 = serie1.temporadas[0]
    temporada2 = serie1.temporadas[1]

    temporada1.adicionar_capitulo(Capitulo("Pilot", 1, datetime(2008, 1, 20)))
    temporada1.adicionar_capitulo(Capitulo("Cat's in the Bag...", 2, datetime(2008, 1, 27)))
    temporada1.adicionar_capitulo(Capitulo("And the Bag's in the River", 3, datetime(2008, 2, 10)))
    temporada1.adicionar_capitulo(Capitulo("Cancer Man", 4, datetime(2008, 2, 17)))
    temporada1.adicionar_capitulo(Capitulo("Gray Matter", 5, datetime(2008, 2, 24)))
    serie1.reproduzir_temporada(1);
    
    temporada2.adicionar_capitulo(Capitulo("Seven Thirty-Seven", 1, datetime(2009, 3, 8)))
    temporada2.adicionar_capitulo(Capitulo("Grilled", 2, datetime(2009, 3, 15)))
    temporada2.adicionar_capitulo(Capitulo("Bit by a Dead Bee", 3   , datetime(2009, 3, 22)))
    temporada2.adicionar_capitulo(Capitulo("Down", 4, datetime(2009, 3, 29)))
    temporada2.adicionar_capitulo(Capitulo("Breakage", 5, datetime(2009, 4, 5)))

    serie1.reproduzir()

    print(f"Série: {serie1.titulo}, Temporada 1 esta completa: {serie1.temporadas[0].verificar_estado()}")

    print(f"Série: {serie1.titulo}, Temporada 2 esta completa: {serie1.temporadas[1].verificar_estado()}")

    print(f"Série: {serie1.titulo}, IMDb Rating: {serie1.imdb_rating}, Visto: {serie1.verificar_estado()}")