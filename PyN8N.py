import requests, json

# URL da API do n8n
url = 'https://n8n.brasfone.pt/api/v1/workflows'

TOKEN_API = "n8n_api_6fb759a1cb4819b4c1c3e2a61352af6eb892a4fccf74c1b820f1ddda6f99782d33424d53b9b042a5"

# Cabeçalhos de autenticação (se necessário)
HEADERS = {
    'X-N8N-API-KEY': 'n8n_api_6fb759a1cb4819b4c1c3e2a61352af6eb892a4fccf74c1b820f1ddda6f99782d33424d53b9b042a5',
    'Content-Type': 'application/json'
}

# Dados para criar ou atualizar um workflow
data = {
    'name': 'Meu novo workflow',
    'nodes': [
        {
            'parameters': {},
            'name': 'Start',
            'type': 'n8n-nodes-base.start',
            'typeVersion': 1,
            'position': [240, 300]
        }
        # Adicione mais nós conforme necessário
    ],
    'connections': {},
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

EXEMPLO =  {
  "name": "Workflow de Exemplo",
  "nodes": [
    {
      "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",
      "name": "Lucao",
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
    "main": [
      {
        "node": "Jira",
        "type": "main",
        "index": 0
      }
    ]
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

# Fazer uma requisição POST para criar um novo workflow
response = requests.post(url, headers=HEADERS, data=json.dumps(data))

# Verificar a resposta
if response.status_code == 200:
    print('Workflow criado com sucesso!')
    print(response.json())
else:
    print(f'Erro ao criar workflow: {response.status_code}')
    print(response.text)
