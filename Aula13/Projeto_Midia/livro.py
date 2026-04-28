from midia import Midia

class Livro(Midia):
    def __init__(self, titulo, ano, autor, isbn):
        super().__init__(titulo, ano)
        self.autor = autor
        self.isbn = isbn
        self.editora = None

    def definir_editora(self, editora):
        self.editora = editora

    def reproduzir(self):
        return f"Lendo o livro '{self.titulo}' de {self.autor} ({self.ano}) - Editora: {self.editora.nome} "