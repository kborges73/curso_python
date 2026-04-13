from televisor import Televisor

if __name__ == "__main__":
    tv1 = Televisor("LG", "Smart TV 4K")
    print(f"Fabricante: {tv1.fabricante}")
    print(f"Modelo: {tv1.modelo}")
    print(f"Canal Atual: {tv1.canal_atual}")
    print(f"Lista de Canais: {tv1.lista_de_canais}")
    print(f"Volume: {tv1.volume}")
    tv1.aumentar_volume()
    print(f"Volume após aumento: {tv1.volume}")
    tv1.diminuir_volume()
    print(f"Volume após diminuição: {tv1.volume}")
    tv1.adicionar_canal("Globo")
    tv1.adicionar_canal("SBT")
    tv1.adicionar_canal("Record")
    print(f"Lista de Canais após adição: {tv1.lista_de_canais}")
    tv1.trocar_canal("SBT")
    print(f"Canal Atual após troca: {tv1.canal_atual}")
    tv1.trocar_canal("AparecidaTV")
    print(f"Canal Atual após troca: {tv1.canal_atual}")

    tv2 = Televisor("Samsung", "Smart TV", canal_atual="Globo", lista_de_canais=["Globo", "SBT", "Record"], volume=10)
    tv2.aumentar_volume();
    print(f"Volume da TV2 após aumento: {tv2.volume}")
    print(f"Canal Atual da TV2: {tv2.canal_atual}")
    print(f"Lista de Canais da TV2: {tv2.lista_de_canais}")