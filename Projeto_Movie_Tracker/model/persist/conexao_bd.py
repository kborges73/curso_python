import psycopg2

class ConexaoBD:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = None

    def conectar(self):
        try:
            self.connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
            print("Conexão com o PostgreSQL estabelecida com sucesso!")
            cursor = self.connection.cursor()
            # Executa uma query simples para verificar a versão do Postgres
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            print("Conexão com o PostgreSQL estabelecida com sucesso!")
            print(f"Versão do banco: {db_version[0]}")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao conectar ao PostgreSQL:", error)

    def fechar_conexao(self):
        if self.connection:
            self.connection.close()
            print("Conexão com o PostgreSQL fechada.")

