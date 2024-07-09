import requests, json
from PypeClass import Funil

# API Token e Headers

API_TOKEN = "e7e7b4d64d34682c8fe269e2afd8497bf9b880f6"

headers = {
    "Content-Type": "application/json",
    "Authorization": API_TOKEN
}

# URLs dos EndPoints

urlPipe = f"https://api.pipedrive.com/v1/pipelines?api_token="

urlStages = f"https://api.pipedrive.com/v1/stages?api_token="

urlDealsFields = f"https://api.pipedrive.com/v1/dealFields?api_token="

urlPersonsFields = f"https://api.pipedrive.com/v1/personFields?api_token="

urlAtv = f"https://api.pipedrive.com/v1/activityTypes?api_token="

urlUsers = f"https://api.pipedrive.com/v1/users?api_token="

urlOrgsFields = f"https://api.pipedrive.com/v1/organizationFields?api_token="

# Funções
def criar_Funil(nome: str, api_token=API_TOKEN):
    payload = {
        "name": nome
    }
    payload = json.dumps(payload)


    response = requests.post(url=f"{urlPipe}{api_token}", data=payload, headers=headers)
    print(response.text, response.status_code)
    # response_data = response.json()
    # data = response_data["data"]
    # return data["id"], data["name"]
    return response.json()

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
        response = requests.post(url=urlStages, data=json.dumps(payload), headers=headers)
        print(f"Criação da Etapa {nome} | Sucesso: {response.status_code}")
        print(response.json())

def criar_Campo(nomes: str, tipo: str, sitio="deals", info=None, api_token=API_TOKEN):
    """
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
    sitio = sitio.lower()
    if sitio == "deals":
        url = urlDealsFields
    elif sitio == "persons":
        url = urlPersonsFields
    else:
        url = urlOrgsFields

    lista_nomes = [nome.strip() for nome in nomes.split(", ")]
    types = {"Texto": "varchar",
             "Escolha": "enum",
             "Data": "date",
             "Moeda": "currency",
             "Status": "status",
             "Numero": "double",
             "Multipla Escolha": "set", 
             "Hora": "time"}
    for nome in lista_nomes:
        payload = {
            "name": nome,
            "field_type": types[tipo]
        }

        if info:
            for key, value in info.items():
                payload[key] = value

        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(response.json())

def criar_TipoAtividade(nome, icon="task", api_token=API_TOKEN):
    payload = {
        "name": nome,
        "icon_key": icon,
        "active_flag": True
    }

    response = requests.post(urlAtv, data=json.dumps(payload), headers=headers)
    return response.json()

def criar_User(nome, email, api_token=API_TOKEN):
    payload = {
        "name": f"{nome}",
        "email": f"{email}",
        "timezone_offset": "+01:00",
        "default_currency": "EUR"
    }

    response = requests.post(url=urlUsers, data=json.dumps(payload), headers=headers)
    print(response.text, response.status_code)

# Criando um Funil

#idfunil, nomefunil = criar_Funil("Siri Cascudo")
#funil = Funil(nomefunil, idfunil)
#print(funil)
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

#criar_Campo("RG, CPF, Peso", "Numero")

# Criando Fases
#fases = "R1: Estudo Inicial, R2: Ajustes e Configurações, R3: Entrega & Treinamento, Fecho, Fase de Suporte & R4"
#criar_Fases(fases, 9)
