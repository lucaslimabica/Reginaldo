import tkinter as tk
from tkinter import messagebox
import PipeANDStages
import re
import random

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reginaldo Alpha Version")
        self.configure(bg='#FFAE69')

        # Container para os frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=False)

        # Dicionário para armazenar os frames
        self.frames = {}

        # Inicialização dos frames
        for F in (HomePage, EtapasFunisPage, CamposPage, AtividadesPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Mostrar a página inicial
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Mostrar um frame para a página dada'''
        frame = self.frames[page_name]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#FFAE69')
        label = tk.Label(self, text="Página Inicial", bg='#FFAE69')
        label.pack(pady=10)

        button1 = tk.Button(self, text="Etapas e Funis", 
                            command=lambda: controller.show_frame("EtapasFunisPage"))
        button2 = tk.Button(self, text="Campos", 
                            command=lambda: controller.show_frame("CamposPage"))
        button3 = tk.Button(self, text="Tipos de Atividade", 
                            command=lambda: controller.show_frame("AtividadesPage"))

        button1.pack(pady=10)
        button2.pack(pady=10)
        button3.pack(pady=10)

class EtapasFunisPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#FFAE69')

        tk.Label(self, text="Nome do Funil:", bg='#FFAE69').pack(padx=10, pady=5)
        self.entrada_nome_funil = tk.Entry(self, width=70)
        self.entrada_nome_funil.pack(padx=10, pady=5)

        self.botao_enviar_funil = tk.Button(self, text="Criar Funil", command=self.criarFunil)
        self.botao_enviar_funil.pack(padx=10, pady=10)

        tk.Label(self, text="Etapas:", bg='#FFAE69').pack(padx=10, pady=5)
        self.entrada_nome_etapa = tk.Entry(self, width=70)
        self.entrada_nome_etapa.pack(padx=10, pady=5)

        # Obter a lista de opções e configurar o dropdown
        self.opcoes = PipeANDStages.get_funil()
        self.variavel_dropdown = tk.StringVar(self)
        self.variavel_dropdown.set(self.opcoes[0])  # Valor padrão
        self.dropdown = tk.OptionMenu(self, self.variavel_dropdown, *self.opcoes)
        self.dropdown.pack(padx=10, pady=5)

        self.botao_enviar_etapa = tk.Button(self, text="Criar Etapa", command=self.criarEtapa)
        self.botao_enviar_etapa.pack(padx=10, pady=10)

        self.button = tk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"))
        self.button.pack(pady=10)

    def criarFunil(self):
        nome = self.entrada_nome_funil.get()
        try:
            PipeANDStages.criar_Funil(nome)
            self.atualizar_dropdown()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao fazer a requisição: {str(e)}")

    def criarEtapa(self):
        nomes = self.entrada_nome_etapa.get()
        nome_opcao = self.variavel_dropdown.get()
        id = self.extrair_id(nome_opcao)
        try:
            PipeANDStages.criar_Fases(nomes, int(id))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao fazer a requisição: {str(e)}")

    def extrair_id(self, opcao):
        match = re.match(r"(\d+)\s+-", opcao)
        if match:
            return match.group(1)
        return None

    def atualizar_dropdown(self):
        novas_opcoes = PipeANDStages.get_funil()
        menu = self.dropdown["menu"]
        menu.delete(0, "end")
        for opcao in novas_opcoes:
            menu.add_command(label=opcao, command=tk._setit(self.variavel_dropdown, opcao))
        self.variavel_dropdown.set(novas_opcoes[0])  # Define o valor padrão

class CamposPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#FFAE69')

        tk.Label(self, text="Criar Campo:", bg='#FFAE69').pack(padx=10, pady=5)
        self.entrada_nome_campo = tk.Entry(self, width=70)
        self.entrada_nome_campo.pack(padx=10, pady=5)

        tk.Label(self, text="Criar Opções (para Escolhas):", bg='#FFAE69').pack(padx=10, pady=5)
        self.entrada_nome_ops = tk.Entry(self, width=70)
        self.entrada_nome_ops.pack(padx=10, pady=5)

        # Lista de Tipos
        self.opcoes = ["Texto", "Escolha", "Data", "Moeda", "Status", "Numero", "Multipla Escolha", "Hora"]
        self.variavel_dropdown_c = tk.StringVar(self)
        self.variavel_dropdown_c.set(self.opcoes[0])  # Valor padrão
        self.dropdown_c = tk.OptionMenu(self, self.variavel_dropdown_c, *self.opcoes)
        self.dropdown_c.pack(padx=10, pady=5)

        self.opcoest = ["Negócios/Leads", "Pessoas", "Organizações"]
        self.variavel_dropdown_ctipo = tk.StringVar(self)
        self.variavel_dropdown_ctipo.set(self.opcoest[0])  # Valor padrão
        self.dropdown_ctipo = tk.OptionMenu(self, self.variavel_dropdown_ctipo, *self.opcoest)
        self.dropdown_ctipo.pack(padx=10, pady=5)

        self.botao_enviar_campo = tk.Button(self, text="Criar Campo", command=self.criarCampo)
        self.botao_enviar_campo.pack(padx=10, pady=10)

        self.button = tk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"))
        self.button.pack(pady=10)

    def criarCampo(self):
        nome = self.entrada_nome_campo.get()
        tipo = self.variavel_dropdown_c.get()
        sitio = self.variavel_dropdown_ctipo.get()
        if sitio == "Negócios/Leads":
            sitio == "deals"
        elif sitio == "Pessoas":
            sitio == "persons"
        dadoscampo = {"edit_flag": True} 
        if tipo == "Escolha" or tipo == "Multipla Escolha":
            random_id = random.randint(1000, 5000) # ID das opções
            ops = self.entrada_nome_ops.get()
            lista_ops = [op.strip() for op in ops.split(",")]
            tmp_lista = [] # Lista que vai ser apendicionada
            for op in lista_ops:
                tmp_lista.append({"id": random_id, "label": op})
                random_id += 1
            dadoscampo["options"] = tmp_lista
                
        PipeANDStages.criar_Campo(nome, tipo, info=dadoscampo)

class AtividadesPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#FFAE69')

        tk.Label(self, text="Nome da Atividade:", bg='#FFAE69').pack(padx=10, pady=5)
        self.entrada_nome_atv = tk.Entry(self, width=70)
        self.entrada_nome_atv.pack(padx=10, pady=5)

        # Lista de Ícones
        tk.Label(self, text="Icon:", bg='#FFAE69').pack(padx=10, pady=5)
        self.opcoesi = ["Call", "Meeting", "Calendar", "Arrow Down", "Email", "Smartphone", "Clip", "Bell"]
        self.variavel_dropdown_i = tk.StringVar(self)
        self.variavel_dropdown_i.set(self.opcoesi[0])  # Valor padrão
        self.dropdown_i = tk.OptionMenu(self, self.variavel_dropdown_i, *self.opcoesi)
        self.dropdown_i.pack(padx=10, pady=5)

        self.botao_enviar_atividade = tk.Button(self, text="Criar Tipo de Atividade", command=self.criarAtv)
        self.botao_enviar_atividade.pack(padx=10, pady=10)

        self.button = tk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"))
        self.button.pack(pady=10)

    def criarAtv(self):
        nome = self.entrada_nome_atv.get()
        icon = self.variavel_dropdown_i.get()
        PipeANDStages.criar_TipoAtividade(nome, icon.lower())

if __name__ == "__main__":
    app = App()
    app.mainloop()
