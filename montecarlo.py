import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
anos = 10
simulacoes = 10  # Ajuste para melhor visualização
retorno_medio = 0.07
desvio_padrao = 0.20
valor_inicial = 10000  # Valor inicial da carteira

# Criando as simulações
anos_simulacao = np.arange(anos + 1)
resultados = np.zeros((simulacoes, anos + 1))
resultados[:, 0] = valor_inicial

# Simulação de Monte Carlo
for i in range(simulacoes):
    for j in range(1, anos + 1):
        retorno_aleatorio = np.random.normal(retorno_medio, desvio_padrao)
        resultados[i, j] = resultados[i, j - 1] * (1 + retorno_aleatorio)

# Exibindo o gráfico
plt.figure(figsize=(10, 6))
plt.plot(anos_simulacao, resultados.T, alpha=0.7)
plt.xlabel("Ano")
plt.ylabel("Valor da Carteira")
plt.title("Simulação de Monte Carlo para Investimento em Ações")
plt.grid(True)
plt.show()
