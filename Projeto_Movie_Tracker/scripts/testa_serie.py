from scripts.generos_enum import Genero
from temporada import Temporada
from capitulo import Capitulo
from serie import Serie
from datetime import datetime

if __name__ == "__main__":

    serie1 = Serie(titulo="Breaking Bad", 
                    imdb_rating=9.5, 
                    generos=[Genero.DRAMA, Genero.POLICIAL],
                    temporadas=[Temporada(2008, 5), Temporada(2009, 5)]
                )
    
    temporada1 = serie1.temporadas[0]
    temporada2 = serie1.temporadas[1]

    temporada1.adicionar_capitulo(Capitulo("Pilot", 1, datetime(2008, 1, 20)))
    temporada1.adicionar_capitulo(Capitulo("Cat's in the Bag...", 2, datetime(2008, 1, 27)))
    temporada1.adicionar_capitulo(Capitulo("And the Bag's in the River", 3, datetime(2008, 2, 10)))
    temporada1.adicionar_capitulo(Capitulo("Cancer Man", 4, datetime(2008, 2, 17)))
    temporada1.adicionar_capitulo(Capitulo("Gray Matter", 5, datetime(2008, 2, 24)))
    
    temporada2.adicionar_capitulo(Capitulo("Seven Thirty-Seven", 1, datetime(2009, 3, 8)))
    temporada2.adicionar_capitulo(Capitulo("Grilled", 2, datetime(2009, 3, 15)))
    temporada2.adicionar_capitulo(Capitulo("Bit by a Dead Bee", 3   , datetime(2009, 3, 22)))
    temporada2.adicionar_capitulo(Capitulo("Down", 4, datetime(2009, 3, 29)))
    temporada2.adicionar_capitulo(Capitulo("Breakage", 5, datetime(2009, 4, 5)))

    temporada1.capitulos[1].marcar_como_visto()
    temporada1.capitulos[2].marcar_como_visto()
    temporada1.capitulos[3].marcar_como_visto()

    print(f"Série: {serie1.titulo}, Temporada 1 esta completa: {serie1.temporadas[0].verificar_estado()}")

    temporada2.capitulos[0].marcar_como_visto()
    temporada2.capitulos[1].marcar_como_visto()
    temporada2.capitulos[2].marcar_como_visto()
    temporada2.capitulos[3].marcar_como_visto()
    temporada2.capitulos[4].marcar_como_visto()

    print(f"Série: {serie1.titulo}, Temporada 2 esta completa: {serie1.temporadas[1].verificar_estado()}")

    print(f"Série: {serie1.titulo}, IMDb Rating: {serie1.imdb_rating}, Visto: {serie1.verificar_estado()}")