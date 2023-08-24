import sqlite3
from db.db_utils import executemany, update, delete, select

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

cursor.execute("""
CREATE TABLE IF NOT EXISTS Frutas (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    situacao TEXT NOT NULL,
    quantidade INTEGER
);
""")

frutas = [
    ("ameixa", "limpa", 5),
    ("banana", "suja", 5),
    ("uva", "suja", 3),
    ("maca", "limpa", 1),
    ("cereja", "limpa", 3)
    
]

executemany(cursor, 'Frutas', ('nome', 'situacao', 'quantidade'), frutas) 
conn.commit()

update(cursor, 'Frutas', 'situacao', 3, 'limpa')
conn.commit()

select(cursor, 'Frutas', 'quantidade', 2)
print(cursor.fetchall())

delete(cursor, 'Frutas', 2)
conn.commit()

