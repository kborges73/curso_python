from midia_player_mixin import MidiaPlayerMixin

class MusicPlayerMixin(MidiaPlayerMixin):
    def play(self, musica):
        print(f"Tocando música: {musica}...")

