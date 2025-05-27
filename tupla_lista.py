class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista para armazenar os livros

    def adicionar_livro(self, titulo, autor, ano):
        livro = (titulo, autor, ano)  # Criando tupla com dados imutáveis
        self.livros.append(livro)  # Adicionando à lista

    def consultar_livros(self):
        print("\nColeção de Livros (Tuplas armazenadas na lista):")
        for livro in self.livros:
            print(f"Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")

# Criando biblioteca
biblioteca = Biblioteca()

# Adicionando livros
biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)
biblioteca.adicionar_livro("A Revolução dos Bichos", "George Orwell", 1945)
biblioteca.adicionar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)

# Consultando livros armazenados
biblioteca.consultar_livros()
