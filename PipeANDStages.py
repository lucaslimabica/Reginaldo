import requests, json, random


# API Token e Headers

API_TOKEN = "e7e7b4d64d34682c8fe269e2afd8497bf9b880f6"

HEADERS = {
    "Content-Type": "application/json"
}

# URLs dos EndPoints

urlPipe = f"https://api.pipedrive.com/v1/pipelines?api_token="

urlStages = f"https://api.pipedrive.com/v1/stages?api_token="

urlDealsFields = f"https://api.pipedrive.com/v1/dealFields?api_token="

urlPersonsFields = f"https://api.pipedrive.com/v1/personFields?api_token="

urlAtv = f"https://api.pipedrive.com/v1/activityTypes?api_token="

urlUsers = f"https://api.pipedrive.com/v1/users?api_token="

urlOrgsFields = f"https://api.pipedrive.com/v1/organizationFields?api_token="

# Úteis para Templates
# -> Eventos
FUNIL_EVENTOS = "Eventos"
FASES_EVENTOS = "Estudo Inicial, Montagem de Proposta, Envio de Proposta, Negociação, Fecho"
ATIVIDADES_EVENTOS = [("Listar Necessidades", "Clip"), ("Planear Evento", "Task"), ("Contacto com Fornecedores", "Call"), ("Enviar Proposta", "Email"), ("Propor Negociação", "Meeting"), ("Enviar Proposta Revisada", "Clip")]
CAMPOS_EVENTOS = [("Tipo de Evento", "deals","Escolha", ("Privado", "Coorporativo", "Casamento")), ("Fornecedor", "deals", "Pessoa"), ("Nr de Convidados", "deals", "Numero"), ("Valor por Convidado", "deals", "Numero"), ("Data para Envio da Proposta", "deals", "Data")]

# Funções
def criar_Funil(nome: str, api_token=API_TOKEN):
    payload = {
        "name": nome
    }
    payload = json.dumps(payload)
    HEADERS["Authorization"] =  f"{api_token}"
    response = requests.post(url=f"{urlPipe}{api_token}", data=payload, headers=HEADERS)
    print(response.text, response.status_code)
    if response.status_code == 201:
        response_data = response.json()
        print(response_data, response.status_code)
        data = response_data["data"]
        return data["id"]
    print(response.json())
    return response.status_code

def get_funil(id="", api_token=API_TOKEN):
    response = requests.get(url=f"https://api.pipedrive.com/v1/pipelines/{id}?api_token={api_token}")
    response_data = response.json()
    if api_token != None:
        data = response_data["data"]
        funis = []
        for funil in data:
            funis.append(f"{funil["id"]} - {funil["name"]}")
        return funis
    else:
        return ["Recarregue o Token de API"]

def criar_Fases(nomes: str, id_funil: int, api_token=API_TOKEN):
    # Divide a string em uma lista de nomes usando a vírgula como delimitador
    lista_nomes = [nome.strip() for nome in nomes.split(", ")]
    for i, nome in enumerate(lista_nomes):
        payload = {
            "name": nome,
            "pipeline_id": id_funil,
            "order_nr": i+1
        }
        HEADERS["Authorization"] =  f"{api_token}"
        response = requests.post(url=f"{urlStages}{api_token}", data=json.dumps(payload), headers=HEADERS)
        print(f"Criação da Etapa {nome} | Sucesso: {response.status_code}")
        print(response.json())

def criar_Campo(nomes: str, tipo: str, sitio="deals", info=None, api_token=API_TOKEN):
    """
    Parâmetros:

    - String com os nomes\n
    - String com o tipo de todos os campos\n
    - String com o local dos campos (deals, persons, orgs)\n
    - Dicict com infos adicionais, como grupo ou descrição\n
    -------------------------------------
    CRIA MAIS DE UM CAMPO POR VEZ
    ### TIPOS DOS CAMPOS
    "varchar" -> Texto
    "enum" -> Escolha Única\n
    "date" -> Data
    "currency" -> Moeda\n
    "status" -> Status
    "int" & "double" -> Número\n
    "set" -> Multipla Escolha
    "time" -> Hora
    """
    sitio = sitio
    if sitio == "deals":
        url = f"{urlDealsFields}{api_token}"
    elif sitio == "persons":
        url = f"{urlPersonsFields}{api_token}"
    elif sitio != "deals" and sitio != "persons":
        url = f"{urlOrgsFields}{api_token}"
    HEADERS["Authorization"] =  f"{api_token}"
    lista_nomes = [nome.strip() for nome in nomes.split(", ")]
    types = {"Texto": "varchar",
             "Escolha": "enum",
             "Data": "date",
             "Moeda": "monetary",
             "Status": "status",
             "Numero": "double",
             "Multipla Escolha": "set", 
             "Hora": "time",
             "Pessoa": "people"}
    for nome in lista_nomes:
        payload = {
            "name": nome,
            "field_type": types[tipo]
        }

        if info:
            for key, value in info.items():
                payload[key] = value

        response = requests.post(url, data=json.dumps(payload), headers=HEADERS)
        print(response.json())

def criar_TipoAtividade(nome, icon="task", api_token=API_TOKEN):
    payload = {
        "name": nome,
        "icon_key": icon,
        "active_flag": True
    }
    HEADERS["Authorization"] =  f"{api_token}"
    response = requests.post(url=f"{urlAtv}{api_token}", data=json.dumps(payload), headers=HEADERS)
    if response.status_code == 201 or response.status_code == 200:
        print(f"Sucesso! Atividade {nome} criado")
    print(response.json())

def criar_User(nome, email, api_token=API_TOKEN):
    payload = {
        "name": f"{nome}",
        "email": f"{email}"
    }
    HEADERS["Authorization"] =  f"{api_token}"
    response = requests.post(url=f"{urlUsers}{api_token}", data=json.dumps(payload), headers=HEADERS)
    print(response.text, response.status_code)

def deletar_Campos(ids = None, api_token=API_TOKEN):
    if ids:
        lista = [numero.strip() for numero in ids.split(",")]
    else:
        lista = [i for i in range(70, 140)]
    for id in lista:
        response = requests.delete(url=f"{urlDealsFields[0:39]}/{id}?api_token={api_token}")
        print(response.json())
        print(f"{urlDealsFields[0:39]}/{id}?api_token={api_token}")
    print(lista)

### Templates ###

def template(funil: str = "Eventos", fases: str = FASES_EVENTOS, campos: list[tuple[str]] = CAMPOS_EVENTOS, atividades: list[tuple[str]] = ATIVIDADES_EVENTOS, api_token: str = API_TOKEN):
    """
    Parâmetros:
    - String com o nome do Funil\n
    - String com as fases\n
    - Lista de tuplas para os campos -> [(nome, sitio, tipo, (opção1, opção2))]\n
    - Lista de tuplas para as atividades -> [(nome, icon)]
    """
    funilID = criar_Funil(funil, api_token=api_token)
    criar_Fases(fases, funilID, api_token=api_token)
    print("FASES CRIADAS")
    for campo in campos:
        if campo[2] == "Escolha" or campo[2] == "Multipla Escolha":
            randomID = random.randint(5000, 6000)
            nome, sitio, tipo, opcoes = campo
            listaOpcoes = []
            for opcao in opcoes:
                listaOpcoes.append({"id": randomID, "label": opcao})
                randomID += 1
            infoCampo = {"options": listaOpcoes}
            criar_Campo(nome, tipo, sitio, info=infoCampo, api_token=api_token)
        else:
            nome, sitio, tipo = campo
            criar_Campo(nome, tipo, sitio, api_token=api_token)
        print(F"Campo {nome} Criado")
    for atividade in atividades:
        nome, icon = atividade
        icon = icon.lower()
        criar_TipoAtividade(nome, icon, api_token=api_token)
        print(f"Tipo {nome} criado")   

dadoscampo = {
    "group_id":1,
    "edit_flag": True,
    "options": [
        {
            "id": 100,
            "label": "Carne"
        },
        {
            "id": 101,
            "label": "Frango"
        },
        {
            "id": 102,
            "label": "Siri"
        }
    ]
}
