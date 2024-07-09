import tkinter as tk
from tkinter import messagebox
import PipeANDStages
import re

# Função para enviar a requisição HTTP
def criarFunil():
    nome = entrada_nome_funil.get()
    try:
        PipeANDStages.criar_Funil(nome)
        atualizar_dropdown()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao fazer a requisição: {str(e)}")

def criarEtapa():
    nomes = entrada_nome_etapa.get()
    #id = entrada_id_funil_etapa.get()
    nome_opcao = variavel_dropdown.get()
    id = extrair_id(nome_opcao)
    try:
        PipeANDStages.criar_Fases(nomes, int(id))
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao fazer a requisição: {str(e)}")

def extrair_id(opcao):
    match = re.match(r"(\d+)\s+-", opcao)
    if match:
        return match.group(1)
    return None

def criarCampo():
    nome = entrada_nome_campo.get()
    tipo = variavel_dropdown_c.get()
    PipeANDStages.criar_Campo(nome, tipo)

def atualizar_dropdown():
    novas_opcoes = PipeANDStages.get_funil()
    menu = dropdown["menu"]
    menu.delete(0, "end")
    for opcao in novas_opcoes:
        menu.add_command(label=opcao, command=tk._setit(variavel_dropdown, opcao))
    variavel_dropdown.set(novas_opcoes[0])  # Define o valor padrão

# Configuração da interface gráfica
root = tk.Tk()
root.title("Reginaldo Alpha Version")
root.configure(bg='#FFAE69')

# Rótulo e caixa de texto para inserir o Nome do Funil
tk.Label(root, text="Nome do Funil:").pack(padx=10, pady=5)
entrada_nome_funil = tk.Entry(root, width=70)
entrada_nome_funil.pack(padx=10, pady=5)

# Botão para Enviar Funil
botao_enviar_funil = tk.Button(root, text="Criar Funil", command=criarFunil)
botao_enviar_funil.pack(padx=10, pady=10)

# Rótulo e caixa de texto para inserir a Etapa do Funil
tk.Label(root, text="Etapas:").pack(padx=10, pady=5)
entrada_nome_etapa = tk.Entry(root, width=70)
entrada_nome_etapa.pack(padx=10, pady=5)

# Obter a lista de opções e configurar o dropdown
opcoes = PipeANDStages.get_funil()
variavel_dropdown = tk.StringVar(root)
variavel_dropdown.set(opcoes[0])  # Valor padrão
dropdown = tk.OptionMenu(root, variavel_dropdown, *opcoes)
dropdown.pack(padx=10, pady=5)

# Botão para Enviar Etapas
botao_enviar_etapa = tk.Button(root, text="Criar Etapa", command=criarEtapa)
botao_enviar_etapa.pack(padx=10, pady=10)

# Rótulo e caixa de texto para inserir um novo Campo
tk.Label(root, text="Criar Campo:").pack(padx=10, pady=5)
entrada_nome_campo = tk.Entry(root, width=70)
entrada_nome_campo.pack(padx=10, pady=5)

# Obter a lista de opções e configurar o dropdown
opcoes = ["varchar","enum","date","currency","status","int","double","set", "time"]
variavel_dropdown_c = tk.StringVar(root)
variavel_dropdown_c.set(opcoes[0])  # Valor padrão
dropdown = tk.OptionMenu(root, variavel_dropdown_c, *opcoes)
dropdown.pack(padx=10, pady=5)

# Botão para Enviar Campos
botao_enviar_campo = tk.Button(root, text="Criar Campo", command=criarCampo)
botao_enviar_campo.pack(padx=10, pady=10)

# Executa a interface gráfica
root.mainloop()
