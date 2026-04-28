from telefone_mixin import TelefoneMixin
from sms_mixin import SMSMixin

class Celular(TelefoneMixin, SMSMixin):
    def __init__(self, marca, modelo, nro_telefone):
        self.marca = marca
        self.modelo = modelo
        self.nro_telefone = nro_telefone

    def ligar(self):
        print(f"{self.marca} {self.modelo} está ligando...")

    def desligar(self):
        print(f"{self.marca} {self.modelo} está desligando...")