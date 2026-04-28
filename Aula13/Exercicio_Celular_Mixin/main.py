from smartphone import Smartphone

if __name__ == "__main__":
    smartphone = Smartphone("Apple", "iPhone 13", "123-456-7890")
    smartphone.fazer_chamada("987-654-3210")
    smartphone.enviar_sms("987-654-3210", "Olá, tudo bem?")
    smartphone.ouvir_musica("Imagine - John Lennon.mp3")    
    smartphone.pausar("Imagine - John Lennon.mp3")
    smartphone.parar("Imagine - John Lennon.mp3")
    smartphone.receber_chamada()
    smartphone.receber_sms("987-654-3210", "Oi, tudo ótimo!")
    smartphone.assistir_video("Video_Exemplo.mp4")  
    smartphone.pausar("Video_Exemplo.mp4")
    smartphone.parar("Video_Exemplo.mp4")