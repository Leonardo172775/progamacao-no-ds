import functools

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f'{self.nome}: {self.nota}'

def comparar_alunos(a, b):
    return (a.nota > b.nota) - (a.nota < b.nota)

# Criando lista de alunos com entrada do usuário
alunos = []
for _ in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos.append(Aluno(nome, nota))

# Ordenando os alunos
alunos_ordenados = sorted(alunos, key=functools.cmp_to_key(comparar_alunos))

# Exibindo a lista ordenada
print("Alunos ordenados por nota:")
print(alunos_ordenados)
