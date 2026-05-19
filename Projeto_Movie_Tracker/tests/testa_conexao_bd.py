from model.persist.conexao_bd import ConexaoBD  

if __name__ == "__main__":
    conexao = ConexaoBD( user="postgres",
        password="karen73",
        host="127.0.0.1",
        port="5432",
        database="meu_banco")
    conexao.conectar()
    conexao.fechar_conexao()
