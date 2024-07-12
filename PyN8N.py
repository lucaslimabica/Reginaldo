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

# Funções Getters

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
    
    with open(fluxo, "w") as file:
        json.dump(conteudo_fluxo, file, indent=2)

# Exemplo de uso da função
altera_Atributo("nome_propriedade", "novo_valor")

atributo_valor = get_Variaveis(get_Nos())
altera_Atributo(propriedade=atributo_valor[0], novo_valor=atributo_valor[1])
# Fazer uma requisição POST para criar um novo workflow
#response = requests.post(url, headers=HEADERS, data=json.dumps(data))
#
## Verificar a resposta
#if response.status_code == 200:
#    print('Workflow criado com sucesso!')
#    print(response.json())
#else:
#    print(f'Erro ao criar workflow: {response.status_code}')
#    print(response.text)
