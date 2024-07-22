import requests


# URL da API do n8n
url = 'https://n8n.brasfone.pt/api/v1/workflows'

TOKEN_API = "n8n_api_6fb759a1cb4819b4c1c3e2a61352af6eb892a4fccf74c1b820f1ddda6f99782d33424d53b9b042a5"

# Cabeçalhos de autenticação (se necessário)
HEADERS = {
    'X-N8N-API-KEY': 'n8n_api_6fb759a1cb4819b4c1c3e2a61352af6eb892a4fccf74c1b820f1ddda6f99782d33424d53b9b042a5',
    'Content-Type': 'application/json'
}

# Nova Versão:

def listaDeModelos() -> list[str]:
  return ["Mudança de Etapa", "Envio de Follow Ups"]

def criaFluxo(nome_do_fluxo: str, nome_do_modelo: str):
   payload = {"Nome": nome_do_fluxo, "Modelo": nome_do_modelo}
   response = requests.post(url="https://n8n.brasfone.pt/webhook/f8e31a1a-29b5-4cbe-8053-bff491c1a4bc", headers=HEADERS, json=payload)
   print(response.json())