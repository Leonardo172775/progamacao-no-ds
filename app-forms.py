import tkinter as tk
from tkinter import messagebox, ttk
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

# Função para visualizar os clientes cadastrados
def visualizar_clientes():
    janela_visualizar = tk.Toplevel(janela)
    janela_visualizar.title("Clientes Cadastrados")
    janela_visualizar.geometry("400x300")

    tree = ttk.Treeview(janela_visualizar, columns=("ID", "Nome", "Email", "Telefone"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Email", text="Email")
    tree.heading("Telefone", text="Telefone")
    tree.pack(fill=tk.BOTH, expand=True)

    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conexao.close()

    for cliente in clientes:
        tree.insert("", tk.END, values=cliente)

# Inicializa o banco de dados
inicializar_banco()

# Criação da interface gráfica
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("300x300")

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

btn_visualizar = tk.Button(janela, text="Visualizar Clientes", command=visualizar_clientes)
btn_visualizar.pack(pady=10)

# Executa a aplicação
janela.mainloop()
