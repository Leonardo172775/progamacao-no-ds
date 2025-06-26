
from collections import Counter

texto = "Python é uma linguagem poderosa e divertida. Python facilita o processamento de texto."

# Converte o texto para minúsculas e divide em palavras 
palavras = texto.lower().split()

# Conta quantas vezes cada palavra aparece 
frequencia = Counter(palavras)

for palavra, contagem in frequencia.items():
    print(f"{palavra}: {contagem}")
