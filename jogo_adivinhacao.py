import random  # Importa o módulo random, que contém funções para gerar números aleatórios.

# Gera um número aleatório entre 1 e 10 e o armazena na variável numero_secreto.
numero_secreto = random.randint(1, 10)
tentativas = 0  # Inicializa a variável tentativas com 0, para contar o número de tentativas do jogador.
max_tentativas = 5  # Define o número máximo de tentativas permitidas.

# Exibe uma mensagem de boas-vindas ao jogador e explica o objetivo do jogo.
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")

# Loop principal do jogo. O jogador terá até o número máximo de tentativas para acertar.
while tentativas < max_tentativas:
    # Solicita ao jogador que insira um número como palpite.
    palpite = int(input("Digite seu palpite: "))

    # Incrementa o número de tentativas a cada palpite do jogador.
    tentativas += 1

    # Verifica se o palpite do jogador é igual ao número secreto.
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break  # Encerra o loop caso o jogador acerte o número.
    # Caso o palpite seja menor que o número secreto, orienta o jogador.
    elif palpite < numero_secreto:
        print("Quase lá! Tente um número maior.")
    # Caso o palpite seja maior que o número secreto, orienta o jogador.
    else:
        print("Quase lá! Tente um número menor.")

    # Informa ao jogador quantas tentativas restantes ele ainda possui.
    if tentativas < max_tentativas:
        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")

# Caso o jogador não acerte o número dentro do limite de tentativas, exibe a mensagem final.
else:
    print("Infelizmente, você não acertou. O número era", numero_secreto)
    print("Fim do jogo!")
