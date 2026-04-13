class Televisor:

    def __init__(self, fabricante, modelo, canal_atual=None, lista_de_canais=[], volume=0):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = canal_atual
        self.lista_de_canais = lista_de_canais
        self.volume = volume

    def aumentar_volume(self):
        self.volume += 1
        return self.volume

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
    
    def trocar_canal(self, novo_canal):
        if novo_canal in self.lista_de_canais:
            self.canal_atual = novo_canal
        else:
            print("Erro, canal inexistente.")
    
    def adicionar_canal(self, novo_canal):
        if novo_canal not in self.lista_de_canais:
            self.lista_de_canais.append(novo_canal)
        else:
            print("Canal existente.")