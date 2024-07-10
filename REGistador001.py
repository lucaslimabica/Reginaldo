import json


# Caminho do arquivo JSON
BASE_TEMPLATES = "C:/Users/lusca/Scripts/Scripts do Pipes/REG001.json"
BASE_LOG = "C:/Users/lusca/Scripts/Scripts do Pipes/REG_LOG001.json"

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

# Criando a base de dados
#criarBase(caminho_arquivo)

# Exemplo de template
template = {
    "nome": "Clínicas",
    "payload": {
        "funil": "Consultas",
        "fases": "Consulta Agendada, Consulta Confirmada, Consulta Realizada, Pós-Consulta",
        "campos": [("Data Agendada", "deals", "Data"), ("Método de Pagamento", "deals", "Escolha", ("Dinheiro", "Multibanco"))],
        "atividades": [("Verficar Data", "task"), ("FU: Ligação", "call")]
    }
}

print(listaTemplates())

# Adicionando o template
#addTemplate(caminho_arquivo, template)

# Obtendo todos os templates
#templates = getTemplate(caminho_arquivo)
#rint("Templates:", templates)

# Obtendo um template específico
#template_clinicas = getTemplate(BASE_TEMPLATES, "Clínicas")
#print("Template Clínicas:", template_clinicas)

#editarTemplate(caminho_arquivo, "Clínicas", novo_template)
