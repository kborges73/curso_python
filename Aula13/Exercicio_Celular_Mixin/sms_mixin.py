class SMSMixin:
    def enviar_sms(self, numero, mensagem):
        print(f"Enviando SMS para {numero}: {mensagem}")    

    def receber_sms(self, numero, mensagem):
        print(f"Recebendo SMS de {numero}: {mensagem}")