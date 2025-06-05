# Solicita ao usuário que insira nomes separados por vírgula
nomes = input("Digite uma lista de nomes separados por vírgula: ").split(",")

# Remove espaços extras dos nomes
nomes = [nome.strip() for nome in nomes]

# Itera sobre a lista usando enumerate e exibe cada nome com seu índice correspondente
for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome}")
