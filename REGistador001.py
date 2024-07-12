import json, datetime, random


# Caminho do arquivo JSON
BASE_TEMPLATES = "C:/Users/lusca/Scripts/Scripts do Pipes/REG001.json"
BASE_LOG = "C:/Users/lusca/Scripts/Scripts do Pipes/REG_LOG001.json"
BASE_API = "C:/Users/lusca/Scripts/Scripts do Pipes/REG_API001.json" 

# Funções de Templates
def criarBase(caminho: str = BASE_TEMPLATES):
    base = {"Pipedrive_Templates": []}
    with open(caminho, "w") as file:
        file.write(json.dumps(base, indent=4))
    print("Base criada com sucesso!")

def addTemplate(template: dict, caminho: str = BASE_TEMPLATES):
    with open(caminho, "r+") as file:
        base = json.load(file)
        base["Pipedrive_Templates"].append(template)
        file.seek(0)
        file.write(json.dumps(base, indent=4))
        file.truncate()
    print("Template adicionado com sucesso!")

def criarTemplate(nome, funil, fases, campos: list[tuple], atividades: list[tuple]):
    template = {
        "nome": nome, 
        "payload": {
            "funil": funil,
            "fases": fases,
            "campos": campos,
            "atividades": atividades
        }
    }
    addTemplate(template)

def getTemplate(caminho: str = BASE_TEMPLATES, nome: str = "Vendas"):
    with open(caminho, "r") as file:
        base = json.load(file)
        if nome:
            for template in base["Pipedrive_Templates"]:
                if template["nome"] == nome:
                    return template
            return None
        else:
            return None

def editarTemplate(nome: str, novo_template: dict, caminho: str = BASE_TEMPLATES):
    with open(caminho, "r+") as file:
        base = json.load(file)
        for i, template in enumerate(base["Pipedrive_Templates"]):
            if template["nome"] == nome:
                base["Pipedrive_Templates"][i] = novo_template
                file.seek(0)
                file.write(json.dumps(base, indent=4))
                file.truncate()
                print("Template editado com sucesso!")
                return
        print("Template não encontrado.")

def listaTemplates(caminho: str = BASE_TEMPLATES) -> list[str]:
    """
    Lista com os nomes de cada template.
    Uso recomendado no menu dropdown.
    """
    with open(caminho, "r") as file:
        lista = []
        base = json.load(file)
        for template in base["Pipedrive_Templates"]:
            lista.append(template["nome"])
        return lista

# Funções de Registo de Logs
def criarBaseLog(caminho: str = BASE_LOG):
    base = {"Log De Dados": []}
    with open(caminho, "w") as file:
        file.write(json.dumps(base, indent=4))
    print("Base criada com sucesso!")

def fazer_LOG(acao: str, api: str = "API Nao Disponibilizada",caminho: str = BASE_LOG):
    with open(caminho, "r+") as file:
        base = json.load(file)
        id_acao = f"{random.randint(0, 1000)}{random.choice("abcdefghijklmnopqrstuvwxyz")}{random.randint(0, 1000)}"
        base["Log De Dados"].append((f"{acao}. API: {api}. ID da Acao: {id_acao}. Data e Hora {datetime.datetime.now()}."))
        file.seek(0)
        file.write(json.dumps(base, indent=4))
        file.truncate()

# Registo de APIs
def criarBaseAPI(caminho: str = BASE_API):
    base = {"Lista APIs": []}
    with open(caminho, "w") as file:
        file.write(json.dumps(base, indent=4))
    print("Base criada com sucesso!")

def salvarAPI(api: str, nome: str = "Cliente Nao Identificado", caminho: str = BASE_API):
    with open(caminho, "r+") as file:
        base = json.load(file)
        base["Lista APIs"].append({"Nome": nome, "API": api})
        file.seek(0)
        file.write(json.dumps(base, indent=4))
        file.truncate()

def listaAPIs(caminho: str = BASE_API):
    "Nomes de cada cliente"
    with open(caminho, "r") as file:
        lista = []
        base = json.load(file)
        for api in base["Lista APIs"]:
            lista.append(api["Nome"])
        return lista
    
def getAPI(nome:str, caminho: str = BASE_API):
    "Retorna pelo nome a API do solicitado cliente"
    with open(caminho, "r") as file:
        base = json.load(file)
        if nome:
            for cliente in base["Lista APIs"]:
                if cliente["Nome"] == nome:
                    return cliente["API"]
            return "API Inválida"
        else:
            return "e7e7b4d64d34682c8fe269e2afd8497bf9b880f6"
        