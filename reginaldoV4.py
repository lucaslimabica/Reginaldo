import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import PipeANDStages
import re
import random
import REGistador001, PyN8N


class AppState:
    def __init__(self):
        self.api_token = None


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Reginaldo Beta Version")
        self.app_state = None
        self.geometry("900x700+50+50")
        self.app_state = AppState()

        style = ttk.Style(self)
        style.theme_use('clam')

        # Configurando estilos personalizados
        style.configure('TFrame', background='#BDECB6')
        style.configure('TLabel', background='#BDECB6', font=('@Microsft YaHei UI', 12))
        style.configure('TEntry', font=('@Microsft YaHei UI', 12))
        style.configure('TButton', font=('@Microsft YaHei UI', 12), padding=6)
        style.configure('Custom.TButton',
                        background='white',
                        foreground='black',
                        font=('@Microsft YaHei UI', 12),
                        borderwidth=0.1,
                        width=25)
        style.map('Custom.TButton',
                  background=[('pressed', '#BDECB6'), ('active', 'black')],
                  foreground=[('disabled', 'gray'), ('active', 'white')])

        # Container para os frames
        container = ttk.Frame(self, style='TFrame')
        container.pack(fill="both", expand=True)
        container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.configure(bg='#BDECB6')

        # Dicionário para armazenar os frames
        self.frames = {}

        # Inicialização dos frames
        for F in (HomePage, EtapasFunisPage, CamposPage, AtividadesPage, UsersPage, TemplatesPage, APIsPage, TemplateAtelier, N8NPage):
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

class HomePage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        label = ttk.Label(self, text="Robot Engine Generator", font=('@Microsft YaHei UI', 20, "bold"))
        label.grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(self, text="(beta version)", font=('@Microsft YaHei UI', 8, "italic")).grid(row=1, column=0, columnspan=2, pady=0)

        label2 = ttk.Label(self, text="Insira o Token de API:")
        label2.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

        self.api_token_entry = ttk.Entry(self, width=50)
        self.api_token_entry.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

        save_button = ttk.Button(self, text="Salvar Token", command=self.save_token, style="Custom.TButton")
        save_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Criação e posicionamento dos botões na grid
        button1 = ttk.Button(self, text="Etapas e Funis", 
                             command=lambda: controller.show_frame("EtapasFunisPage"), style="Custom.TButton")
        button2 = ttk.Button(self, text="Campos Personalizados", 
                             command=lambda: controller.show_frame("CamposPage"), style="Custom.TButton")
        button3 = ttk.Button(self, text="Tipos de Atividade", 
                             command=lambda: controller.show_frame("AtividadesPage"), style="Custom.TButton")
        button4 = ttk.Button(self, text="Usuários", 
                             command=lambda: controller.show_frame("UsersPage"), style="Custom.TButton")
        button5 = ttk.Button(self, text="Galeria de Templates", 
                             command=lambda: controller.show_frame("TemplatesPage"), style="Custom.TButton")
        button6 = ttk.Button(self, text="Biblioteca de APIs", 
                             command=lambda: controller.show_frame("APIsPage"), style="Custom.TButton")
        button7 = ttk.Button(self, text="Atelier de Templates", 
                             command=lambda: controller.show_frame("TemplateAtelier"), style="Custom.TButton")
        button8 = ttk.Button(self, text="Fabrica de Automações", 
                             command=lambda: controller.show_frame("N8NPage"), style="Custom.TButton")

        # Posicionando os botões na grid
        ttk.Label(self, text="Criação do Ambiente Pipedrive").grid(row=5, column=0, padx=5, pady=10, columnspan=2)
        button1.grid(row=6, column=0, padx=5, pady=10)
        button2.grid(row=6, column=1, padx=5, pady=10)
        ttk.Label(self, text="Personalização do Pipedrive").grid(row=7, column=0, padx=5, pady=10, columnspan=2)
        button3.grid(row=8, column=0, padx=5, pady=10)
        button4.grid(row=8, column=1, padx=5, pady=10)
        ttk.Label(self, text="Ferramentas Avançadas").grid(row=9, column=0, padx=5, pady=10, columnspan=2)
        button5.grid(row=10, column=0, padx=5, pady=10)
        button6.grid(row=10, column=1, padx=5, pady=10)
        button7.grid(row=11, column=0, padx=5, pady=10)
        button8.grid(row=11, column=1, padx=5, pady=10)

    def save_token(self):
        token = self.api_token_entry.get()
        print(f"Token salvo: {token}")
        
class EtapasFunisPage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state

        ttk.Label(self, text="Criação de Funil e Fases", font=('@Microsft YaHei UI', 20, "bold")).pack(pady=10)

        ttk.Label(self, text="Nome do Funil:", font=('@Microsft YaHei UI', 12)).pack(padx=10, pady=5)
        self.entrada_nome_funil = ttk.Entry(self, width=50)
        self.entrada_nome_funil.pack(padx=10, pady=5)

        self.botao_enviar_funil = ttk.Button(self, text="Criar Funil", command=self.criarFunil, style="Custom.TButton")
        self.botao_enviar_funil.pack(padx=10, pady=10)

        ttk.Label(self, text="Etapas:", font=('@Microsft YaHei UI', 12)).pack(padx=10, pady=5)
        self.entrada_nome_etapa = ttk.Entry(self, width=50)
        self.entrada_nome_etapa.pack(padx=10, pady=5)

        self.selecao_funil = ttk.Label(self, text="Selecione um Funil", font=('@Microsft YaHei UI', 12))
        self.selecao_funil.pack(pady=10, padx=10)

        # Adicionando um Combobox (dropdown)
        self.variavel_dropdown = tk.StringVar()
        self.dropdown = ttk.Combobox(self, textvariable=self.variavel_dropdown, values=PipeANDStages.get_funil(api_token=self.app_state.api_token), style='TCombobox')
        self.dropdown.pack(pady=5, padx=10)

        self.button_atl = ttk.Button(self, text="Atualizar Funis", command=self.atualizar_dropdown, style="Custom.TButton")
        self.button_atl.pack(pady=10)

        self.botao_enviar_etapa = ttk.Button(self, text="Criar Etapa", command=self.criarEtapa, style="Custom.TButton")
        self.botao_enviar_etapa.pack(padx=10, pady=10)

        self.token_label = ttk.Label(self, text="")
        self.token_label.pack(pady=10, padx=10)

        self.button = ttk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"), style="Custom.TButton")
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
        self.dropdown['values'] = novas_opcoes
        if novas_opcoes:
            self.variavel_dropdown.set(novas_opcoes[0])

    def tkraise(self, aboveThis=None):
        if self.app_state.api_token:
            self.token_label.config(text=f"Token de API: {self.app_state.api_token}")
        else:
            self.token_label.config(text="Token de API não definido")
        super().tkraise(aboveThis)

class CamposPage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state

        ttk.Label(self, text="Criação de Campos", font=('@Microsft YaHei UI', 20)).pack(pady=10)

        ttk.Label(self, text="Criar Campo:", font=('@Microsft YaHei UI', 12)).pack(padx=10, pady=5)
        self.entrada_nome_campo = ttk.Entry(self, width=70)
        self.entrada_nome_campo.pack(padx=10, pady=5)

        ttk.Label(self, text="Criar Opções (para Escolhas):", font=('@Microsft YaHei UI', 12)).pack(padx=10, pady=5)
        self.entrada_nome_ops = ttk.Entry(self, width=70)
        self.entrada_nome_ops.pack(padx=10, pady=5)

        # Adicionando um Combobox (dropdown)
        ttk.Label(self, text="Selecione o Tipo:", font=('@Microsft YaHei UI', 12)).pack(padx=10, pady=5)
        self.variavel_dropdown_tipo = tk.StringVar()
        self.dropdown_tipo = ttk.Combobox(self, textvariable=self.variavel_dropdown_tipo, values=["Texto", "Escolha", "Data", "Moeda", "Status", "Numero", "Multipla Escolha", "Hora"], style='TCombobox')
        self.dropdown_tipo.pack(pady=5, padx=10)
        
        ttk.Label(self, text="Selecione o Sítio:").pack(padx=10, pady=5)
        self.variavel_dropdown = tk.StringVar()
        self.dropdown = ttk.Combobox(self, textvariable=self.variavel_dropdown, values=["Negócios/Leads", "Pessoas", "Organizações"], style='TCombobox')
        self.dropdown.pack(pady=5, padx=10)

        self.botao_enviar_campo = ttk.Button(self, text="Criar Campo", command=self.criarCampo, style="Custom.TButton")
        self.botao_enviar_campo.pack(padx=10, pady=10)

        self.token_label = ttk.Label(self, text="")
        self.token_label.pack(pady=10, padx=10)

        self.button = ttk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"), style="Custom.TButton")
        self.button.pack(pady=10)

    def tkraise(self, aboveThis=None):
        if self.app_state.api_token:
            self.token_label.config(text=f"Token de API: {self.app_state.api_token}")
        else:
            self.token_label.config(text="Token de API não definido")
        super().tkraise(aboveThis)

    def criarCampo(self):
        nome = self.entrada_nome_campo.get()
        tipo = self.variavel_dropdown_tipo.get()
        sitio = self.variavel_dropdown.get()
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

class AtividadesPage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state

        ttk.Label(self, text="Criação de Atividades", font=('@Microsft YaHei UI', 20, "bold")).pack(pady=10)

        ttk.Label(self, text="Nome da Atividade:", font=('@Microsft YaHei UI', 12)).pack(padx=10, pady=5)
        self.entrada_nome_atv = ttk.Entry(self, width=70)
        self.entrada_nome_atv.pack(padx=10, pady=5)

        # Lista de Ícones
        ttk.Label(self, text="Icon:").pack(padx=10, pady=5)

        self.variavel_dropdown = tk.StringVar()
        self.dropdown = ttk.Combobox(self, textvariable=self.variavel_dropdown, values=["Call", "Meeting", "Calendar", "Arrow Down", "Email", "Smartphone", "Clip", "Bell"], style='TCombobox')
        self.dropdown.pack(pady=5, padx=10)

        self.botao_enviar_atividade = ttk.Button(self, text="Criar Tipo de Atividade", command=self.criarAtv, style="Custom.TButton")
        self.botao_enviar_atividade.pack(padx=10, pady=10)

        self.token_label = ttk.Label(self, text="")
        self.token_label.pack(pady=10, padx=10)

        self.button = ttk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"), style="Custom.TButton")
        self.button.pack(pady=10)

    def tkraise(self, aboveThis=None):
        if self.app_state.api_token:
            self.token_label.config(text=f"Token de API: {self.app_state.api_token}")
        else:
            self.token_label.config(text="Token de API não definido")
        super().tkraise(aboveThis)

    def criarAtv(self):
        nome = self.entrada_nome_atv.get()
        icon = self.variavel_dropdown.get()
        PipeANDStages.criar_TipoAtividade(nome, icon.lower(), api_token=self.app_state.api_token)

class UsersPage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state

        ttk.Label(self, text="Criação de Usuários", font=('@Microsft YaHei UI', 22, "bold")).pack(pady=10)

        ttk.Label(self, text="Nome do Usuário:", font=('@Microsft YaHei UI', 12)).pack(padx=10, pady=5)
        self.entrada_nome_user = ttk.Entry(self, width=70)
        self.entrada_nome_user.pack(padx=10, pady=5)

        ttk.Label(self, text="Email do Usuário:", font=('@Microsft YaHei UI', 12)).pack(padx=10, pady=5)
        self.entrada_email_user = ttk.Entry(self, width=70)
        self.entrada_email_user.pack(padx=10, pady=5)

        self.botao_enviar_user = ttk.Button(self, text="Criar Usuário", command=self.criarUser, style="Custom.TButton")
        self.botao_enviar_user.pack(padx=10, pady=10)

        self.token_label = ttk.Label(self, text="")
        self.token_label.pack(pady=10, padx=10)

        self.button = ttk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"), style="Custom.TButton")
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

class TemplatesPage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state

        ttk.Label(self, text="Galeria de Templates", font=('@Microsft YaHei UI', 20, "bold")).pack(pady=10)

        ttk.Label(self, text="Selecione o Template:", font=('@Microsft YaHei UI', 12)).pack(padx=10, pady=5)

        self.variavel_dropdown = tk.StringVar()
        self.dropdown = ttk.Combobox(self, textvariable=self.variavel_dropdown, values=REGistador001.listaTemplates(), style='TCombobox')
        self.dropdown.pack(pady=5, padx=10)

        self.botao_enviar_template = ttk.Button(self, text="Criar Pipedrive", command=self.usarTemplate, style="Custom.TButton")
        self.botao_enviar_template.pack(padx=10, pady=10)

        self.token_label = ttk.Label(self, text="")
        self.token_label.pack(pady=10, padx=10)

        self.button = ttk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"), style="Custom.TButton")
        self.button.pack(pady=10)

    def tkraise(self, aboveThis=None):
        if self.app_state.api_token:
            self.token_label.config(text=f"Token de API: {self.app_state.api_token}")
        else:
            self.token_label.config(text="Token de API não definido")
        super().tkraise(aboveThis)

    def usarTemplate(self):
        nome_modelo = self.variavel_dropdown.get()
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

class TemplateAtelier(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        label = ttk.Label(self, text="Atelier de Templates", font=('@Microsft YaHei UI', 20, "bold"))
        label.grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self, text="Nome do Template:", font=("@Microsft YaHei UI", 12), justify="left").grid(row=1, column=0, columnspan=2, pady=10)
        self.entrada_nome_template = ttk.Entry(self, width=50)
        self.entrada_nome_template.grid(row=2, column=0, columnspan=2, pady=10)

        ttk.Label(self, text="Nome do Funil:", font=("@Microsft YaHei UI", 12), justify="left").grid(row=3, column=0, pady=10)
        self.entrada_funil_template = ttk.Entry(self, width=50)
        self.entrada_funil_template.grid(row=3, column=1, pady=10)

        ttk.Label(self, text="Fases:", font=("@Microsft YaHei UI", 12), justify="left").grid(row=4, column=0, pady=10)
        self.entrada_fases_template = ttk.Entry(self, width=50)
        self.entrada_fases_template.grid(row=4, column=1, pady=10)         

        ttk.Label(self, text="Campos Texto:", font=("@Microsft YaHei UI", 12), justify="left").grid(row=5, column=0, pady=10)
        self.entrada_textos_template = ttk.Entry(self, width=50)
        self.entrada_textos_template.grid(row=5, column=1, pady=10)

        ttk.Label(self, text="Campos Número:", font=("@Microsft YaHei UI", 12), justify="left").grid(row=6, column=0, pady=10)
        self.entrada_numeros_template = ttk.Entry(self, width=50)
        self.entrada_numeros_template.grid(row=6, column=1, pady=10)

        ttk.Label(self, text="Campos Data:", font=("@Microsft YaHei UI", 12), justify="left").grid(row=7, column=0, pady=10)
        self.entrada_datas_template = ttk.Entry(self, width=50)
        self.entrada_datas_template.grid(row=7, column=1, pady=10)

        ttk.Label(self, text="Campos Opção:", font=("@Microsft YaHei UI", 12), justify="left").grid(row=8, column=0, pady=10)
        self.entrada_escolha_template = ttk.Entry(self, width=50)
        self.entrada_escolha_template.grid(row=8, column=1, pady=10)

        ttk.Label(self, text="Opções (op1, op2, op3):", font=("@Microsft YaHei UI", 12), justify="left").grid(row=9, column=0, pady=10)
        self.entrada_ops_template = ttk.Entry(self, width=50)
        self.entrada_ops_template.grid(row=9, column=1, pady=10)

        ttk.Label(self, text="Atividades (nome, icon):", font=("@Microsft YaHei UI", 12), justify="left").grid(row=10, column=0, pady=10)
        self.entrada_atividades_template = ttk.Entry(self, width=50)
        self.entrada_atividades_template.grid(row=10, column=1, pady=10)

        self.token_label = ttk.Label(self, text="")
        #self.token_label.grid(row=10, columnspan=2, column=0, pady=10)

        self.botao_enviar_template = ttk.Button(self, text="Salvar Template", command=self.salvarTemplate, style="Custom.TButton")
        self.botao_enviar_template.grid(row=11, column=0, pady=10, columnspan=2)

        self.button = ttk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"), style="Custom.TButton")
        self.button.grid(row=12, columnspan=2, column=0, pady=10)

    def salvarTemplate(self):
        novo_template = {"nome": "REGifone",
                              "payload": {
                                  "funil": "Cloud Solutions",
                                  "fases": "Estudo Inicial, Fase de Proposta, Negociação, Fecho",
                                  "campos": [("Envio de Proposta", "deals", "Data"), ("Produto/Serviço", "deals", "Escolha", ("Dev Sofwate", "Support Software"))],
                                  "atividades": [] 
                              }}
        corpo_template = novo_template["payload"]
        novo_template["nome"] = self.entrada_nome_template.get()
        corpo_template["funil"] = self.entrada_funil_template.get()
        corpo_template["fases"] = self.entrada_fases_template.get()
        
        ### Atividades ###
        # Expressão regular para encontrar tuplas
        PADRAO_TUPLA_ATV = re.compile(r'\(([^)]+)\)')
        # Encontrar todas as tuplas na string
        tuples = PADRAO_TUPLA_ATV.findall(self.entrada_atividades_template.get())
        # Lista para armazenar os dicionários resultantes
        atividades = []
        # Processar cada tupla
        for t in tuples:
            # Dividir a tupla em partes
            nome, tipo = map(str.strip, t.split(','))
            # Criar um dicionário para a tupla
            atividades.append((nome, tipo))
        corpo_template["atividades"] = atividades
        
        ### Campos ###
        lista_campos = []
        if self.entrada_numeros_template.get():
            lista_num = [num.strip() for num in self.entrada_numeros_template.get().split(", ")]
            for num in lista_num:
                num = (num, "deals", "Numero")
                lista_campos.append(num)
        if self.entrada_textos_template.get():
            lista_txt = [txt.strip() for txt in self.entrada_textos_template.get().split(", ")]
            for txt in lista_txt:
                txt = (txt, "deals", "Texto")
                lista_campos.append(txt)
        if self.entrada_datas_template.get():
            lista_data = [data.strip() for data in self.entrada_datas_template.get().split(", ")]
            for data in lista_data:
                data = (data, "deals", "Data")
                lista_campos.append(data)
        if self.entrada_escolha_template.get():
            lista_escolhas = [escolha.strip() for escolha in self.entrada_escolha_template.get().split(", ")] # Lista dos campos de escolha
            lista_ops = [op for op in self.entrada_ops_template.get().split("/")]
            lista_ops_tratada = [] # Lista das opções já separadas
            for op in lista_ops:
                lista_ops_tratada.append((op.split(", ")))
            lista_campos_escolha = []
            for i in range(len(lista_escolhas)):
                lista_campos_escolha.append((lista_escolhas[i], "deals", "Escolha", lista_ops_tratada[i]))
            for campo in lista_campos_escolha:
                lista_campos.append(campo)
        corpo_template["campos"] = lista_campos
        
        REGistador001.criarTemplate(
            nome=novo_template["nome"],
            funil=corpo_template["funil"],
            fases=corpo_template["fases"],
            campos=corpo_template["campos"],
            atividades=corpo_template["atividades"]
        )
        REGistador001.fazer_LOG(f"Criacao de Template: {novo_template['nome']}", api="LOCAL")
        self.atualizar_dropdown()
        print(lista_campos_escolha)
        print(novo_template)

    def tkraise(self, aboveThis=None):
        if self.app_state.api_token:
            self.token_label.config(text=f"Token de API: {self.app_state.api_token}")
        else:
            self.token_label.config(text="Token de API não definido")
        super().tkraise(aboveThis)

    def atualizar_dropdown(self):
        novas_opcoes = REGistador001.listaTemplates()
        TemplatesPage.dropdown['values'] = novas_opcoes
        if novas_opcoes:
            TemplatesPage.variavel_dropdown.set(novas_opcoes[0])
        
class N8NPage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state

        ttk.Label(self, text="Fábrica de Automações", font=('@Microsft YaHei UI', 20, "bold")).pack(pady=10)

        ttk.Label(self, text="Crie um Novo Fluxo").pack(padx=10, pady=5)

        ttk.Label(self, text="Nome do Fluxo:").pack(padx=10, pady=5)
        self.entrada_nome_fluxo = ttk.Entry(self, width=50)
        self.entrada_nome_fluxo.pack(padx=10, pady=5)

        # Lista de Modelos
        ttk.Label(self, text="Selecione o Modelo de Fluxo").pack(padx=10, pady=5)
        self.variavel_dropdown = tk.StringVar()
        self.dropdown = ttk.Combobox(self, textvariable=self.variavel_dropdown, values=PyN8N.getListaModelos(), style='TCombobox')
        self.dropdown.pack(pady=5, padx=10)
        self.dropdown.bind("<<ComboboxSelected>>", self.on_select)
        ### CONTINUAR DAQUI!
        self.label_etapa_gatilho = ttk.Label(self, text="Etapa Gatilho:")
        self.entrada_tipo_atv = ttk.Entry(self, width=50)

        self.label_atividade_gatilho = ttk.Label(self, text="Título da Atividade:")
        self.entrada_tipo_atv = ttk.Entry(self, width=50)

        # Salvar Modelo
        self.botao_selecionar_modelo = ttk.Button(self, text="Salvar Modelo", command=self.selecionarModelo, style="Custom.TButton")
        self.botao_selecionar_modelo.pack(padx=10, pady=10)

        self.token_label = ttk.Label(self, text="")
        self.token_label.pack(pady=10, padx=10)

        self.button = ttk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"), style="Custom.TButton")
        self.button.pack(pady=10)

    def tkraise(self, aboveThis=None):
        if self.app_state.api_token:
            self.token_label.config(text=f"Token de API: {self.app_state.api_token}")
        else:
            self.token_label.config(text="Token de API não definido")
        super().tkraise(aboveThis)

    def selecionarModelo(self):
        EtapasFunisPage.atualizar_dropdown(self)
        self.tkraise()

    # Função que faz aparecer os campos de cada modelo de fluxo
    def on_select(self, event):
        selected_value = self.variavel_dropdown.get()
        if selected_value == "Criacao de Atividade":
            self.label_atividade_gatilho.pack(padx=10, pady=5)
            self.entrada_tipo_atv.pack(padx=10, pady=5)
        else:
            self.label_atividade_gatilho.pack_forget()
            self.entrada_tipo_atv.pack_forget()

    def atualizar_dropdown(self):
        novas_opcoes = REGistador001.listaAPIs()
        self.dropdown['values'] = novas_opcoes
        if novas_opcoes:
            self.variavel_dropdown.set(novas_opcoes[0])


class APIsPage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state

        ttk.Label(self, text="Galeria de APIs", font=('@Microsft YaHei UI', 20, "bold")).pack(pady=10)

        ttk.Label(self, text="Adicione uma Nova API").pack(padx=10, pady=5)

        ttk.Label(self, text="Nome da API:").pack(padx=10, pady=5)
        self.entrada_nome_api = ttk.Entry(self, width=70)
        self.entrada_nome_api.pack(padx=10, pady=5)

        ttk.Label(self, text="Token da API:").pack(padx=10, pady=5)
        self.entrada_token_api = ttk.Entry(self, width=70)
        self.entrada_token_api.pack(padx=10, pady=5)

        # Criar API
        self.botao_criar_api = ttk.Button(self, text="Salvar API", command=self.salvarAPI, style="Custom.TButton")
        self.botao_criar_api.pack(padx=10, pady=10)

        # Lista de APIs
        ttk.Label(self, text="Selecione a API").pack(padx=10, pady=5)

        self.variavel_dropdown = tk.StringVar()
        self.dropdown = ttk.Combobox(self, textvariable=self.variavel_dropdown, values=REGistador001.listaAPIs(), style='TCombobox')
        self.dropdown.pack(pady=5, padx=10)

        # Selecionar API
        self.botao_selecionar_api = ttk.Button(self, text="Selecionar API", command=self.selecionarAPI, style="Custom.TButton")
        self.botao_selecionar_api.pack(padx=10, pady=10)

        self.token_label = ttk.Label(self, text="")
        self.token_label.pack(pady=10, padx=10)

        self.button = ttk.Button(self, text="Voltar para a Página Inicial", 
                           command=lambda: controller.show_frame("HomePage"), style="Custom.TButton")
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
        self.tkraise()
        self.selecionarAPI(modo="Criacao")
        REGistador001.fazer_LOG(acao=f"Criacao de API. Cliente: {nome}", api=self.app_state.api_token)
        self.atualizar_dropdown()

    def selecionarAPI(self, modo="Selecao"):
        if modo == "Selecao":
            nome = self.variavel_dropdown.get()
        else:
            nome = self.entrada_nome_api.get()
        self.app_state.api_token = REGistador001.getAPI(nome)
        EtapasFunisPage.atualizar_dropdown(self)
        self.tkraise()

    def atualizar_dropdown(self):
        novas_opcoes = REGistador001.listaAPIs()
        self.dropdown['values'] = novas_opcoes
        if novas_opcoes:
            self.variavel_dropdown.set(novas_opcoes[0])
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
