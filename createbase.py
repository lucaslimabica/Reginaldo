import sqlite3

conn = sqlite3.connect("REG.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS log (
        ID_ACAO INTEGER PRIMARY KEY AUTOINCREMENT,
        ACAO TEXT NOT NULL,
        DATA_HORA TEXT
    )""")

conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS templates (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        FUNIL TEXT NOT NULL,
        FASES TEXT NOT NULL,
        CAMPOS TEXT NOT NULL,
        ATIVIDADES TEXT NOT NULL,
        DATA_HORA_CRIACAO TEXT
    )""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS apis (
        ID_API INTEGER PRIMARY KEY AUTOINCREMENT,
        TOKEN TEXT NOT NULL,
        CLIENTE TEXT NOT NULL,
        DATA_HORA_CRIACAO TEXT
    )""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS modelos_automacoes (
        ID_MODELO INTEGER PRIMARY KEY AUTOINCREMENT,
        ACAO TEXT NOT NULL,
        DATA_HORA_CRIACAO TEXT
    )""")

conn.commit()
conn.close()