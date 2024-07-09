import sqlite3
import datetime
import ast
import json
import PipeANDStages

conn = sqlite3.connect("REG.db")
cursor = conn.cursor()

def fazer_LOG(acao, api="SEM API"):
    """
    Log do que foi feito.
    :param acao: Texto da ação realizada
    :param api: API utilizada. Caso não fornecida, preenche-se com um valor base
    """
    cursor.execute("""INSERT INTO log_dados (ACAO, DATA_HORA, CLIENTE_API) VALUES (?, ?, ?)""", (acao, str(datetime.datetime.now()), api))
    conn.commit()
    conn.close()

def carregar_Template(id) -> dict:
    """
    Reorna um Dicionário Pronto para cada chave ser usada
    como parâmetro para a função template.

    funil: str -> string
    fases: str -> string
    campos: str -> lista de tuplas: [("Nome", "Sítio", ("Opção1", "Opção2"))]
    atividades: str -> lista de tuplas: [("Nome", "Icon")]
    """
    retorno = {
        "funil": "",
        "fases": "",
        "campos_texto": [],
        "atividades": []
    }

    ### Pegar Funil ###
    cursor.execute("SELECT FUNIL FROM templates_pipe WHERE ID = ?", (id,))
    funil = cursor.fetchone()[0]
    retorno["funil"] = funil

    ### Pegar Fases ###
    cursor.execute("SELECT FASES FROM templates_pipe WHERE ID = ?", (id,))
    fases = cursor.fetchone()[0]
    retorno["fases"] = fases

    ### Pegar Fases ###
    cursor.execute("SELECT ATIVIDADES FROM templates_pipe WHERE ID = ?", (id,))
    atividades_string = cursor.fetchone()[0]
    # Separando atividada por atividada
    atividades = [atividade.strip() for atividade in atividades_string.split("), ")]
    
    # Tratando o nome e o tipo
    atividades[0] = atividades[0][1:]
    atividades[0] += ")"
    atividades[-1] = atividades[-1][:-1]

    # Criando a lista que vai ser parâmetro da função final
    for atividade in atividades:
        nome, tipo = atividade.split(", ")
        nome = nome[2:-1]
        nome = nome.replace('"', '')
        tipo = tipo[1:-1]
        tipo = tipo.replace('"', '')
        retorno["atividades"].append((nome, tipo))

    ### Pegar Campos Texto ###
    cursor.execute("SELECT CAMPOS_TEXT FROM templates_pipe WHERE ID = ?", (id,))
    campos_string = cursor.fetchone()[0]
    # Separando campo por campo
    campos = [campo.strip() for campo in campos_string.split("), ")]
    
    # Tratando o primeiro e último campo
    campos[0] = campos[0][1:]
    campos[0] += ")"
    campos[-1] = campos[-1][:-1]

    # Criando a lista que vai ser parâmetro da função final
    for campo in campos:
        nome, sitio = campo.split(", ")
        nome = nome[2:-1]
        sitio = sitio[1:-2]
        retorno["campos_texto"].append((nome, sitio, "Texto"))
    
    return retorno

#funil = "Vendas"
#fases = "Estudo Inicial, Envio de Proposta, Negociação, Fecho"
#campos = '[("Nome", "deals"), ("Pedido", "deals")]'
#atividades = '[("FU Ligação", "call"), ("Montar Proposta", "clip"), ("Enviar Proposta", "email")]'
#cursor.execute("INSERT INTO templates_pipe (FUNIL, FASES, CAMPOS_TEXT, ATIVIDADES) VALUES (?, ?, ?, ?)", (funil, fases, campos, atividades))
#conn.commit()
dicio = carregar_Template(2)
print(dicio["atividades"])
PipeANDStages.template(funil=dicio["funil"], fases=dicio["fases"], campos=dicio["campos_texto"], atividades=dicio["atividades"], api_token="e7e7b4d64d34682c8fe269e2afd8497bf9b880f6")