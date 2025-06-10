# Definindo uma lista de números inteiros
numeros = [10, 20, 30, 40, 50]

# Função para calcular a soma dos elementos na lista
def calcular_soma(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

# Função para encontrar o maior número na lista
def encontrar_maior(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

# Adicionando o número 60 à lista
numeros.append(60)

# Exibindo a lista original
print("Lista de números:", numeros)

# Calculando e exibindo a soma dos elementos na lista
soma = calcular_soma(numeros)
print("Soma dos números:", soma)

# Encontrando e exibindo o maior número na lista
maior_numero = encontrar_maior(numeros)
print("Maior número na lista:", maior_numero)

# Função para calcular a média dos elementos na lista
def calcular_media(lista):
    soma = calcular_soma(lista)
    return soma / len(lista)

# Calculando e exibindo a média dos elementos na lista
media = calcular_media(numeros)
print("Média dos números:", media)