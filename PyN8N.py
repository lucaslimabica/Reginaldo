import requests, json


# URL da API do n8n
url = 'https://n8n.brasfone.pt/api/v1/workflows'

TOKEN_API = "n8n_api_6fb759a1cb4819b4c1c3e2a61352af6eb892a4fccf74c1b820f1ddda6f99782d33424d53b9b042a5"

# Cabeçalhos de autenticação (se necessário)
HEADERS = {
    'X-N8N-API-KEY': 'n8n_api_6fb759a1cb4819b4c1c3e2a61352af6eb892a4fccf74c1b820f1ddda6f99782d33424d53b9b042a5',
    'Content-Type': 'application/json'
}

CAMINHO_EXEMPLO = "C:/Users/lusca/Scripts/Scripts do Pipes/FluxoBase001.json"
CAMINHO_MODELOS = "C:/Users/lusca/Scripts/Scripts do Pipes/ListaDeFluxos.json"

DATA = {
  "name": "Workflow Template",
  "nodes": [
    {
      "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
      "name": "Reginaldo",
      "webhookId": "string",
      "disabled": True,
      "notesInFlow": True,
      "notes": "string",
      "type": "n8n-nodes-base.Jira",
      "typeVersion": 1,
      "executeOnce": False,
      "alwaysOutputData": False,
      "retryOnFail": False,
      "maxTries": 0,
      "waitBetweenTries": 0,
      "onError": "stopWorkflow",
      "position": [
        -100,
        80
      ],
      "parameters": {
        "additionalProperties": {}
      },
      "credentials": {
        "jiraSoftwareCloudApi": {
          "id": "35",
          "name": "jiraApi"
        }
      }
    }
  ],
  "connections": {
    "Pipedrive Trigger1": {
      "main": [
        [
          {
            "node": "Edit Fields1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Edit Fields1": {
      "main": [
        [
          {
            "node": "Pipedrive1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "saveExecutionProgress": True,
    "saveManualExecutions": True,
    "saveDataErrorExecution": "all",
    "saveDataSuccessExecution": "all",
    "executionTimeout": 3600,
    "errorWorkflow": "VzqKEW0ShTXA5vPj",
    "timezone": "America/New_York",
    "executionOrder": "v1"
  },
  "staticData": {
    "lastId": 1
  }
}

# Funções Getters

def getListaModelos(lista = CAMINHO_MODELOS):
  """
  Permite pegar todos os modelos de fluxos
  Retorna uma lista de string do nome_modelo do fluxo N8N.
  """
  listam = []
  with open(CAMINHO_MODELOS, "r") as file:
    lista = json.load(file)
    for modelo in lista["modelos"]:
       listam.append(modelo["nome_modelo"])
  return listam

def get_Modelo(nome_modelo):
  with open(CAMINHO_MODELOS, "r") as file:
    lista = json.load(file)
    for modelo in lista["modelos"]:
       if modelo["nome_modelo"] == nome_modelo:
        nos = [no for no in modelo['nodes']]
    for i, no in enumerate(nos):
      if no["type"].split(".")[-1] == "set":
        print(f"Nó {i + 1} - {no["name"]}")
    escolha = int(input("Qual Nó deve ser alterado?"))
  return nos[escolha - 1]


def get_Nos(caminho=CAMINHO_EXEMPLO) -> dict:
  """
  Permite apenas pegar os nós Edit Fields (SET)
  Retorna o nó completo como dicionário
  """
  with open(caminho, "r") as file:
    fluxo = json.load(file)
    nos = [no for no in fluxo['nodes']]
    for i, no in enumerate(nos):
      if no["type"].split(".")[-1] == "set":
        print(f"Nó {i + 1} - {no["name"]}")
    escolha = int(input("Qual Nó deve ser alterado?"))
  return nos[escolha - 1]

def get_Variaveis(no):
  parametros = no["parameters"]
  assignments = parametros["assignments"]
  assignments_lista = assignments["assignments"]
  print("Qual Atributo deve ser alterado?")
  for i, atributo in enumerate(assignments_lista):
    print(f"{i + 1}º : {atributo["name"]} - Valor: {atributo["value"]}")
    print("-" * 50)
  escolha = int(input(">>> "))
  novo_valor = input("Insira a nova fórmula: ")
  return assignments_lista[escolha - 1]['name'], novo_valor
    #for key, value in atributo.items():
    #  print(f"{key} - {value}")

def altera_Atributo(propriedade, novo_valor, fluxo=CAMINHO_EXEMPLO):
    """
    Altera um atributo específico de um nó no fluxo de trabalho
    """
    with open(fluxo, "r") as file:
        conteudo_fluxo = json.load(file)
    
    nos = [no for no in conteudo_fluxo['nodes']]
    for i, no in enumerate(nos):
        if no["type"].split(".")[-1] == "set":
            parametros = no["parameters"]
            assignments = parametros["assignments"]
            assignments_lista = assignments["assignments"]
            for atributo in assignments_lista:
                if atributo["name"] == propriedade:
                    atributo["value"] = novo_valor
                    print(f"Atributo {propriedade} alterado para: {novo_valor}")
                    break
    
    return conteudo_fluxo
    #with open(fluxo, "w") as file:
    #    json.dump(conteudo_fluxo, file, indent=2)


#atributo_valor = get_Variaveis(get_Nos())
#altera_Atributo(propriedade=atributo_valor[0], novo_valor=atributo_valor[1])

# Criador de Lista de Nós
def criar_Fluxo(novo_nome, fluxo=CAMINHO_EXEMPLO):
  """
  Faz o POST do novo fluxo com base no modelo selecionado.
  
  :param novo_nome: String com o nome do novo fluxo
  :param fluxo: Caminho do arquivo com o modelo do fluxo. Default: CAMINHO_EXEMPLO
  """
  with open(fluxo, "r") as file:
    conteudo_fluxo = json.load(file)
    file.close()
  nos = conteudo_fluxo['nodes']
  novo_fluxo = DATA
  novo_fluxo["name"] = novo_nome
  novo_fluxo['nodes'] = nos
  response = requests.post(url, headers=HEADERS, data=json.dumps(novo_fluxo))
  if response.status_code == 200:
    print('Workflow criado com sucesso!')
    # print(response.json())
  else:
    print(f'Erro ao criar workflow: {response.status_code}')
    print(response.text)

#criar_Fluxo("TestePyN8N000")

   