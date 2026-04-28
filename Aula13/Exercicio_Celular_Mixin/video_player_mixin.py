from midia_player_mixin import MidiaPlayerMixin 

class VideoPlayerMixin(MidiaPlayerMixin):
    def play(self, video):
        print(f"Tocando vídeo: {video}...")

