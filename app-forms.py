import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para conectar ao banco de dados e criar a tabela
def inicializar_banco():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

# Função para salvar os dados do cliente
def salvar_cliente():
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    if not nome or not email or not telefone:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos antes de salvar.")
        return

    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)", (nome, email, telefone))
    conexao.commit()
    conexao.close()

    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    limpar_formulario()

# Função para limpar os campos do formulário
def limpar_formulario():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

# Inicializa o banco de dados
inicializar_banco()

# Criação da interface gráfica
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("300x250")

# Labels e campos de entrada
tk.Label(janela, text="Nome:").pack(pady=5)
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack()

tk.Label(janela, text="E-mail:").pack(pady=5)
entry_email = tk.Entry(janela, width=40)
entry_email.pack()

tk.Label(janela, text="Telefone:").pack(pady=5)
entry_telefone = tk.Entry(janela, width=40)
entry_telefone.pack()

# Botões
btn_salvar = tk.Button(janela, text="Salvar", command=salvar_cliente)
btn_salvar.pack(pady=10)

btn_limpar = tk.Button(janela, text="Limpar", command=limpar_formulario)
btn_limpar.pack()

# Executa a aplicação
janela.mainloop()
