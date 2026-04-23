from dataclasses import dataclass
from datetime import datetime  

@dataclass
class Capitulo:
    titulo: str
    numero: int
    data_exibicao: datetime
    visto: bool = False

    def verificar_disponibilidade(self):
        if self.data_exibicao != None:
            return True
        return False
    
