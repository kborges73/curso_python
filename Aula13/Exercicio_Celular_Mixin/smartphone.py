from celular import Celular
from video_player_mixin import VideoPlayerMixin
from music_player_mixin import MusicPlayerMixin

class Smartphone (Celular, MusicPlayerMixin, VideoPlayerMixin):
    def __init__(self, marca, modelo, nro_telefone):
        super().__init__(marca, modelo, nro_telefone)

    def ouvir_musica(self, arquivo):
        if (arquivo.endswith('.mp3')):
            #self.play(self, arquivo)
            MusicPlayerMixin.play(self, arquivo)
        else :
            print("Arquivo de música inválido. Por favor, forneça um arquivo .mp3")

    def pausar(self, arquivo):
        self.pause()

    def parar(self, arquivo):
        self.stop()

    def assistir_video(self, arquivo):
        if (arquivo.endswith('.mp4')):
            #self.play(self, arquivo)
            VideoPlayerMixin.play(self, arquivo)
        else:   
            print("Arquivo de vídeo inválido. Por favor, forneça um arquivo .mp4")

    