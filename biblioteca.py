1#CRIANDO A CLASE LIVRO
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Gênero: {self.genero} | Quantidade: {self.quantidade}"

#CRIANDO A LISTA DE LIVROS
livros = []

# FUNÇÃO PARA FAZER O CADASTRAMENTO DE LIVROS
def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Gênero: ")
    try:
        quantidade = int(input("Quantidade disponível: "))
        livro = Livro(titulo, autor, genero, quantidade)
        livros.append(livro)
        print("Livro cadastrado com sucesso!\n")
    except ValueError:
        print("Erro: quantidade deve ser um número inteiro.\n")

# FUNÇÃO PARA LISTAR TODOS OS LIVROS CADASTRADOS
def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.\n")
    else:
        for livro in livros:
            print(livro)
        print()

# FUNÇÃO PARA BUSCAR LIVROS POR TITULOS
def buscar_por_titulo():
    titulo = input("Digite o título a buscar: ")
    encontrados = [livro for livro in livros if livro.titulo.lower() == titulo.lower()]
    if encontrados:
        for livro in encontrados:
            print(livro)
    else:
        print("Livro não encontrado.\n")

import matplotlib.pyplot as plt
# FUNÇÃO PARA GERAR GRAFICOS DE ACORDO COM GENERO E QUANTIDADE
def gerar_grafico():
    if not livros:
        print("Nenhum livro para gerar gráfico.\n")
        return

    genero_dict = {}
    for livro in livros:
        if livro.genero in genero_dict:
            genero_dict[livro.genero] += livro.quantidade
        else:
            genero_dict[livro.genero] = livro.quantidade

    generos = list(genero_dict.keys())
    quantidades = list(genero_dict.values())

    plt.figure(figsize=(8,5))
    plt.bar(generos, quantidades, color='skyblue')
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade")
    plt.title("Quantidade de Livros por Gênero")
    plt.tight_layout()
    plt.show()

# MENU PARA USO DO SISTEMA
def menu():
    while True:
        print("===== BIBLIOTECA =====")
        print("1. Cadastrar novo livro")
        print("2. Listar livros")
        print("3. Buscar livro por título")
        print("4. Gerar gráfico de livros por gênero")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            buscar_por_titulo()
        elif opcao == '4':
            gerar_grafico()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.\n")

# INICIAR O MENU
menu()
