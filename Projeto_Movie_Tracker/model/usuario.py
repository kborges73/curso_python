from dataclasses import dataclass, field
from model.playlist import Playlist
from model.credencial import Credencial   

@dataclass
class Usuario:
    """
    CONCEITO: COMPOSIÇÃO / ASSOCIAÇÃO
    O Utilizador possui e gere as suas Playlists.
    """
    nome: str   
    acesso: Credencial
    nivel_acesso: str
    playlists: dict[str, Playlist] = field(default_factory=dict)

    def criar_playlist(self, nome: str, descricao: str):
        nova_p = Playlist(nome, descricao)
        self.playlists[nome] = nova_p
        print(f"✨ Nova playlist '{nome}' criada para {self.nome}.")

