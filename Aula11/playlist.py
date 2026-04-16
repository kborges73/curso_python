from dataclasses import dataclass
from dataclasses import field
from filme import Filme

@dataclass
class Playlist:
    """
    CONCEITO: AGREGAÇÃO
    Uma Playlist contém múltiplos objetos Filme. 
    Se a playlist for apagada, os objetos Filme continuam a existir.
    """
    nome: str
    descricao: str
    filmes: list[Filme] = field(default_factory=list)

    def adicionar_filme(self, filme: Filme):
        if filme not in self.filmes:
            self.filmes.append(filme)
            print(f"✅ '{filme.titulo}' adicionado à playlist '{self.nome}'")

    def remover_filme(self, filme: Filme):
        if filme in self.filmes:
            self.filmes.remove(filme)
            print(f"❌ '{filme.titulo}' removido da playlist '{self.nome}'")
        else:
            print(f"⚠️ '{filme.titulo}' não encontrado na playlist '{self.nome}'")  