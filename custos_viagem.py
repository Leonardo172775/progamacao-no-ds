class Veiculo:
    def calcular_custo(self, distancia):
        raise NotImplementedError("Este método deve ser sobrescrito pelas subclasses")

class Carro(Veiculo):
    def calcular_custo(self, distancia):
        return distancia * 0.8  # Custo de R$0,80 por km

class Bicicleta(Veiculo):
    def calcular_custo(self, distancia):
        return distancia * 0.28  # Custo de R$0,28 por km

class Caminhao(Veiculo):
    def calcular_custo(self, distancia):
        return distancia * 1.32  # Custo de R$1,32 por km

def calcular_custo_total(veiculos, distancia):
    total_custo = sum(veiculo.calcular_custo(distancia) for veiculo in veiculos)
    return total_custo

# Criando objetos de diferentes tipos de veículos
veiculos = [Carro(), Bicicleta(), Caminhao()]
distancia = 200  # Distância da viagem

# Calculando o custo total da viagem
custo_total = calcular_custo_total(veiculos, distancia)
print(f"Custo total da viagem de {distancia} km para todos os veículos: R${custo_total:.2f}")
