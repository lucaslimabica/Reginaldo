import sqlite3

conn = sqlite3.connect("REG.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS log_dados (
        ID_ACAO INTEGER PRIMARY KEY AUTOINCREMENT,
        ACAO TEXT NOT NULL,
        DATA_HORA TEXT,
        CLIENTE_API TEXT
    )""")

conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS templates_pipe (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        FUNIL TEXT NOT NULL,
        FASES TEXT NOT NULL,
        CAMPOS_INT TEXT,
        CAMPOS_TEXT TEXT,
        CAMPOS_OPS TEXT,
        CAMPOS_DATA TEXT,
        ATIVIDADES TEXT NOT NULL,
        DATA_HORA_CRIACAO TEXT
    )""")

cursor.execute("DROP TABLE IF EXISTS templates")

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