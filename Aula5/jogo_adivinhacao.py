import random

def iniciar_jogo():
    # 1. Configuração inicial
    numero_secreto = random.randint(1, 100)
    palpites = [] # usando uma lista para armazenar os palpites do usuário
    
    print("========================================")
    print("🎮 BEM-VINDO AO JOGO DE ADIVINHAÇÃO!")
    print("Estou pensando num número entre 1 e 100.")
    print("========================================\n")

    # 2. Ciclo principal (Simulando um Do-While)
    while True:
        try:
            # Pedir o palpite ao jogador
            entrada = input(f"Tentativa {len(palpites) + 1} - Qual é o seu palpite? ")
            
            # Validar se a entrada é numérica
            if not entrada.isdigit():
                print("⚠️ Por favor, digite um número inteiro válido.")
                continue #volta para o início do loop para pedir um novo palpite
            
            palpite = int(entrada)
            
            # Guardar o palpite no histórico
            palpites.append(palpite)

            # 3. Lógica de Verificação
            if palpite == numero_secreto:
                print(f"\n🎉 PARABÉNS! Acertou no número {numero_secreto}!")
                break # Sai do ciclo pois o jogo terminou
            
            elif palpite < numero_secreto:
                print("🔼 Mais alto! Tente novamente.")
            else:
                print("🔽 Mais baixo! Tente novamente.")
                
        except KeyboardInterrupt:
            print("\n\nJogo interrompido pelo utilizador. Até à próxima!")
            return

    # 4. Exibição das Estatísticas Finais
    print("\n" + "="*40)
    print("📊 RESUMO DA PARTIDA")
    print(f"Total de tentativas: {len(palpites)}")
    print(f"Números tentados: {palpites}")
    print("="*40)

if __name__ == "__main__":
    iniciar_jogo()