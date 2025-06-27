# a) Lista com pelo menos 8 cidades
cidades = ["Curitiba", "São Paulo", "Rio de Janeiro", "Recife", "Salvador", "Brasília", "Fortaleza", "Porto Alegre"]

# b) Solicita ao usuário a sequência de caracteres
busca = input("Digite uma letra ou sequência de caracteres para buscar nas cidades: ").lower()

# c) Filtra cidades que contenham a sequência (ignorando maiúsculas/minúsculas)
resultado = [cidade for cidade in cidades if busca in cidade.lower()]

# d) Exibe os resultados ou informa se não houve correspondência
if resultado:
    print("Cidades encontradas:")
    for cidade in resultado:
        print("-", cidade)
else:
    print("Nenhuma cidade encontrada com esse critério de busca.")
