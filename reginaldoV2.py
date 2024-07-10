import tkinter as tk
from tkinter import messagebox
import PipeANDStages
import re
import random
import REGistador001 


class AppState:
    def __init__(self):
        self.api_token = None

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reginaldo Beta Version")
        self.configure(bg='#FFAE69')
        self.app_state = None

        self.app_state = AppState()

        # Container para os frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=False)

        # Dicionário para armazenar os frames
        self.frames = {}

        # Inicialização dos frames
        for F in (HomePage, EtapasFunisPage, CamposPage, AtividadesPage, UsersPage, TemplatesPage, APIsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self, app_state=self.app_state)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Mostrar a página inicial
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Mostrar um frame para a página dada'''
        frame = self.frames[page_name]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state
        self.configure(bg='#FFAE69')
        label = tk.Label(self, text="Página Inicial", bg='#FFAE69')
        label.pack(pady=10)

        labeL2 = tk.Label(self, text="Digite seu token de API:", bg= "#FFAE69")
        labeL2.pack(pady=10, padx=10)

        self.api_token_entry = tk.Entry(self)
        self.api_token_entry.pack(pady=10, padx=10)

        save_button = tk.Button(self, text="Salvar Token",
                                command=self.save_token)
        save_button.pack()

        button1 = tk.Button(self, text="Etapas e Funis", 
                            command=lambda: controller.show_frame("EtapasFunisPage"))
        button2 = tk.Button(self, text="Campos Personalizados", 
                            command=lambda: controller.show_frame("CamposPage"))
        button3 = tk.Button(self, text="Tipos de Atividade", 
                            command=lambda: controller.show_frame("AtividadesPage"))
        button4 = tk.Button(self, text="Usuários", 
                            command=lambda: controller.show_frame("UsersPage"))
        button5 =tk.Button(self, text="Galeria de Templates", 
                            command=lambda: controller.show_frame("TemplatesPage"))
        button6 =tk.Button(self, text="Galeria de APIs", 
                            command=lambda: controller.show_frame("APIsPage"))

        button1.pack(pady=10)
        button2.pack(pady=10)
        button3.pack(pady=10)
        button4.pack(pady=10)
        button5.pack(pady=10)
        button6.pack(pady=10)

    def save_token(self):
        self.app_state.api_token = self.api_token_entry.get()

class EtapasFunisPage(tk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#FFAE69')
        self.app_state = app_state

        tk.Label(self, text="Nome do Funil:", bg='#FFAE69').pack(padx=10, pady=5)
        self.entrada_nome_funil = tk.Entry(self, width=70)
        self.entrada_nome_funil.pack(padx=10, pady=5)

        self.botao_enviar_funil = tk.Button(self, text="Criar Funil", command=self.criarFunil)
        self.botao_enviar_funil.pack(padx=10, pady=10)

        tk.Label(self, text="Etapas:", bg='#FFAE69').pack(padx=10, pady=5)
        self.entrada_nome_etapa = tk.Entry(self, width=70)
        self.entrada_nome_etapa.pack(padx=10, pady=5)

        # Obter a lista de opções e configurar o dropdown
        self.opcoes = PipeANDStages.get_funil(api_token=self.app_state.api_token)
        self.variavel_dropdown = tk.StringVar(self)
        self.variavel_dropdown.set(self.opcoes[0])  # Valor padrão
        self.dropdown = tk.OptionMenu(self, self.variavel_dropdown, *self.opcoes)
        self.dropdown.pack(padx=10, pady=5)

        self.button_atl = tk.Button(self, text="Atualizar Dropdown", command=self.atualizar_dropdown)
        self.button_atl.pack(pady=10)

        self.botao_enviar_etapa = tk.Button(self, text="Criar Etapa", command=self.criarEtapa)
        self.botao_enviar_etapa.pack(padx=10, pady=10)

        self.token_label = tk.Label(self, text="")
        self.token_label.pack(pady=10, padx=10)

        self.button = tk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"))
        self.button.pack(pady=10)

    def criarFunil(self):
        nome = self.entrada_nome_funil.get()
        try:
            PipeANDStages.criar_Funil(nome, api_token=self.app_state.api_token)
            self.atualizar_dropdown()
            REGistador001.fazer_LOG(f"Criação de Funil {nome}", self.app_state.api_token)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao fazer a requisição: {str(e)}")

    def criarEtapa(self):
        nomes = self.entrada_nome_etapa.get()
        nome_opcao = self.variavel_dropdown.get()
        id = self.extrair_id(nome_opcao)
        try:
            PipeANDStages.criar_Fases(nomes, int(id), api_token=self.app_state.api_token)
            REGistador001.fazer_LOG(f"Criação das Etapas: {nomes} (id:{id})", self.app_state.api_token)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao fazer a requisição: {str(e)}")

    def extrair_id(self, opcao):
        match = re.match(r"(\d+)\s+-", opcao)
        if match:
            return match.group(1)
        return None

    def atualizar_dropdown(self):
        novas_opcoes = PipeANDStages.get_funil(api_token=self.app_state.api_token)
        menu = self.dropdown["menu"]
        menu.delete(0, "end")
        for opcao in novas_opcoes:
            menu.add_command(label=opcao, command=tk._setit(self.variavel_dropdown, opcao))
        self.variavel_dropdown.set(novas_opcoes[0])  # Define o valor padrão

    def tkraise(self, aboveThis=None):
        if self.app_state.api_token:
            self.token_label.config(text=f"Token de API: {self.app_state.api_token}")
        else:
            self.token_label.config(text="Token de API não definido")
        super().tkraise(aboveThis)

class CamposPage(tk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#FFAE69')
        self.app_state = app_state

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

        self.token_label = tk.Label(self, text="")
        self.token_label.pack(pady=10, padx=10)

        self.button = tk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"))
        self.button.pack(pady=10)

    def tkraise(self, aboveThis=None):
        if self.app_state.api_token:
            self.token_label.config(text=f"Token de API: {self.app_state.api_token}")
        else:
            self.token_label.config(text="Token de API não definido")
        super().tkraise(aboveThis)

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
                
        PipeANDStages.criar_Campo(nome, tipo, info=dadoscampo, api_token=self.app_state.api_token)
        REGistador001.fazer_LOG(f"Criação dos Campos: {nome}", self.app_state.api_token)

class AtividadesPage(tk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#FFAE69')
        self.app_state = app_state

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

        self.token_label = tk.Label(self, text="")
        self.token_label.pack(pady=10, padx=10)

        self.button = tk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"))
        self.button.pack(pady=10)

    def tkraise(self, aboveThis=None):
        if self.app_state.api_token:
            self.token_label.config(text=f"Token de API: {self.app_state.api_token}")
        else:
            self.token_label.config(text="Token de API não definido")
        super().tkraise(aboveThis)

    def criarAtv(self):
        nome = self.entrada_nome_atv.get()
        icon = self.variavel_dropdown_i.get()
        PipeANDStages.criar_TipoAtividade(nome, icon.lower(), api_token=self.app_state.api_token)

class UsersPage(tk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#FFAE69')
        self.app_state = app_state

        tk.Label(self, text="Nome do Usuário:", bg='#FFAE69').pack(padx=10, pady=5)
        self.entrada_nome_user = tk.Entry(self, width=70)
        self.entrada_nome_user.pack(padx=10, pady=5)

        tk.Label(self, text="Email do Usuário:", bg='#FFAE69').pack(padx=10, pady=5)
        self.entrada_email_user = tk.Entry(self, width=70)
        self.entrada_email_user.pack(padx=10, pady=5)

        self.botao_enviar_user = tk.Button(self, text="Criar Usuário", command=self.criarUser)
        self.botao_enviar_user.pack(padx=10, pady=10)

        self.token_label = tk.Label(self, text="")
        self.token_label.pack(pady=10, padx=10)

        self.button = tk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"))
        self.button.pack(pady=10)

    def tkraise(self, aboveThis=None):
        if self.app_state.api_token:
            self.token_label.config(text=f"Token de API: {self.app_state.api_token}")
        else:
            self.token_label.config(text="Token de API não definido")
        super().tkraise(aboveThis)

    def criarUser(self):
        nome = self.entrada_nome_user.get()
        email = self.entrada_email_user.get()
        PipeANDStages.criar_User(nome, email, api_token=self.app_state.api_token)
        REGistador001.fazer_LOG(f"Criação de User {email}", self.app_state.api_token)

class TemplatesPage(tk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#FFAE69')
        self.app_state = app_state

        tk.Label(self, text="Template:", bg='#FFAE69').pack(padx=10, pady=5)
        self.opcoest = REGistador001.listaTemplates()
        self.variavel_dropdown_t = tk.StringVar(self)
        self.variavel_dropdown_t.set(self.opcoest[0])  # Valor padrão
        self.dropdown_t = tk.OptionMenu(self, self.variavel_dropdown_t, *self.opcoest)
        self.dropdown_t.pack(padx=10, pady=5)

        self.botao_enviar_template = tk.Button(self, text="Criar Pipedrive", command=self.usarTemplate)
        self.botao_enviar_template.pack(padx=10, pady=10)

        self.token_label = tk.Label(self, text="")
        self.token_label.pack(pady=10, padx=10)

        self.button = tk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"))
        self.button.pack(pady=10)

    def tkraise(self, aboveThis=None):
        if self.app_state.api_token:
            self.token_label.config(text=f"Token de API: {self.app_state.api_token}")
        else:
            self.token_label.config(text="Token de API não definido")
        super().tkraise(aboveThis)

    def usarTemplate(self):
        nome_modelo = self.variavel_dropdown_t.get()
        modelpai = REGistador001.getTemplate(nome=nome_modelo)
        model = modelpai["payload"]
        PipeANDStages.template(
                                funil=model["funil"],
                                fases=model["fases"],
                                campos=model["campos"],
                                atividades=model["atividades"],
                                api_token=self.app_state.api_token
                            )
        REGistador001.fazer_LOG(acao=f"Uso de Template: {nome_modelo}", api=self.app_state.api_token)

class APIsPage(tk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#FFAE69')
        self.app_state = app_state

        tk.Label(self, text="Adicione uma Nova API:", bg='#FFAE69').pack(padx=10, pady=5)

        tk.Label(self, text="Nome da API:", bg='#FFAE69').pack(padx=10, pady=5)
        self.entrada_nome_api = tk.Entry(self, width=70)
        self.entrada_nome_api.pack(padx=10, pady=5)

        tk.Label(self, text="Token da API:", bg='#FFAE69').pack(padx=10, pady=5)
        self.entrada_token_api = tk.Entry(self, width=70)
        self.entrada_token_api.pack(padx=10, pady=5)

        # Criar API
        self.botao_criar_api = tk.Button(self, text="Salvar API", command=self.salvarAPI)
        self.botao_criar_api.pack(padx=10, pady=10)

        # Lista de APIs
        tk.Label(self, text="Selecione a API", bg='#FFAE69').pack(padx=10, pady=5)
        self.opcoesapi = REGistador001.listaAPIs()
        self.variavel_dropdown_api = tk.StringVar(self)
        self.variavel_dropdown_api.set(self.opcoesapi[0])  # Valor padrão
        self.dropdown_api = tk.OptionMenu(self, self.variavel_dropdown_api, *self.opcoesapi)
        self.dropdown_api.pack(padx=10, pady=5)

        # Selecionar API
        self.botao_selecionar_api = tk.Button(self, text="Selecionar API", command=self.selecionarAPI)
        self.botao_selecionar_api.pack(padx=10, pady=10)

        self.token_label = tk.Label(self, text="")
        self.token_label.pack(pady=10, padx=10)

        self.button = tk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"))
        self.button.pack(pady=10)

    def tkraise(self, aboveThis=None):
        if self.app_state.api_token:
            self.token_label.config(text=f"Token de API: {self.app_state.api_token}")
        else:
            self.token_label.config(text="Token de API não definido")
        super().tkraise(aboveThis)

    def salvarAPI(self):
        nome = self.entrada_nome_api.get()
        token = self.entrada_token_api.get()
        REGistador001.salvarAPI(api=token, nome=nome)
        self.selecionarAPI(modo="Criacao")
        REGistador001.fazer_LOG(acao=f"Criação de API. Cliente: {nome}", api=self.app_state.api_token)
        self.atualizar_dropdown()

    def selecionarAPI(self, modo="Selecao"):
        if modo == "Selecao":
            nome = self.variavel_dropdown_api.get()
        else:
            nome = self.entrada_nome_api.get()
        self.app_state.api_token = REGistador001.getAPI(nome)

    def atualizar_dropdown(self):
        novas_opcoes = REGistador001.listaAPIs()
        menu = self.dropdown_api["menu"]
        menu.delete(0, "end")
        for opcao in novas_opcoes:
            menu.add_command(label=opcao, command=tk._setit(self.variavel_dropdown_api, opcao))
        self.variavel_dropdown_api.set(novas_opcoes[0])  # Define o valor padrão
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
