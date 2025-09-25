import json

# Define a classe Cliente
class Cliente:
    def __init__(self, id, nome, email, pagamentos=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.pagamentos = pagamentos if pagamentos is not None else []

    # Converte o objeto Cliente em um dicionário
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "pagamentos": self.pagamentos
        }

# Lista de pagamentos (exemplo)
pagamentos
