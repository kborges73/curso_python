from equipamento import Equipamento

class EquipamentoSonoro(Equipamento):
    def __init__(self,volume,stereo):
        super().__init__(ligado = False)
        self.volume = volume
        self.stereo = stereo

    def aumentar_volume(self):
        if self.volume >= 10:
            print(f"Volume máximo!")
        else:
            self.volume += 1
            print(f"Volume atual: {self.volume}")

    def diminuir_volume(self):
        if self.volume <= 0:
            print(f"Volume mínimo! ")
        else:
            self.volume -=1
            print(f"Volume atual {self.volume}")

    def ligar_mono(self):
        self.stereo = False

    def ligar_stereo(self):
        self.stereo = True

    #Sobrescrita do método ligar() da classe Equipamento
    def liga(self):
        super().liga()
        self.volume = 5

if __name__ == "__main__":
    CaixaDeSom = EquipamentoSonoro(3,True)

    print(f"Volume inicial: {CaixaDeSom.volume}")
    print(f"Status Stereo: {CaixaDeSom.stereo}")

    CaixaDeSom.liga()
    print(f"Volume incial depois de ligado: {CaixaDeSom.volume}")

    CaixaDeSom.aumentar_volume()
    CaixaDeSom.aumentar_volume()
    CaixaDeSom.aumentar_volume()

    CaixaDeSom.diminuir_volume()
    CaixaDeSom.diminuir_volume()

    CaixaDeSom.ligar_mono()
    print(f"Status Stereo: {CaixaDeSom.stereo}")

    CaixaDeSom.ligar_stereo()
    print(f"Status Stereo: {CaixaDeSom.stereo}")