# Lê o número inteiro positivo n
n = int(input("Digite a quantidade de números inteiros: "))

# Inicializa a lista
lista = []

# Lê n números inteiros e os adiciona à lista
for _ in range(n):
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)

# Lê o número inteiro x
x = int(input("Digite o número que deseja verificar na lista: "))

# Verifica se x pertence à lista
if x in lista:
    print(f"{x} pertence à lista.")
else:
    print(f"{x} não pertence à lista.")
