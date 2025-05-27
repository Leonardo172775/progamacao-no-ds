class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b

# Testando os métodos estáticos
resultado_soma = Calculadora.somar(10, 5)
resultado_subtracao = Calculadora.subtrair(10, 5)

print(f"Soma: {resultado_soma}")
print(f"Subtração: {resultado_subtracao}")
