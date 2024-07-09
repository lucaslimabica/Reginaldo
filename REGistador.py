import sqlite3
import datetime

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

