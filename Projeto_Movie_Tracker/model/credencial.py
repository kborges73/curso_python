from dataclasses import dataclass

@dataclass
class Credencial:
    login: str # O email será usado como nome de usuário para login
    senha: str