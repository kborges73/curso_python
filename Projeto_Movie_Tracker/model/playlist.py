from dataclasses import dataclass
from dataclasses import field
from model.video import Video
from model.usuario import Usuario

@dataclass
class Playlist:
    """
    CONCEITO: AGREGAÇÃO
    Uma Playlist contém múltiplos objetos Video. 
    Se a playlist for apagada, os objetos Video continuam a existir.
    Uma Playlist pertence a um único Usuario, mas um Usuario pode ter várias Playlists.
    Se a Playlist for apagada, o Usuario associados continuam a existir.
    """
    nome: str
    descricao: str
    videos: list[Video] = field(default_factory=list)
    usuario: Usuario

    def adicionar_video(self, video: Video):
        if video not in self.videos:
            self.videos.append(video)
            print(f"✅ '{video.titulo}' adicionado à playlist '{self.nome}'")

    def remover_video(self, video: Video):
        if video in self.videos:
            self.videos.remove(video)
            print(f"❌ '{video.titulo}' removido da playlist '{self.nome}'")
        else:
            print(f"⚠️ '{video.titulo}' não encontrado na playlist '{self.nome}'")  