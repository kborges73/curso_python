from dataclasses import dataclass

@dataclass
class Equipamento:
    ligado: bool
    
    def liga(self):
        print("Ligado!")
        self.ligado = True

    def desliga(self):
        print("Desligado!")
        self.ligado = False
