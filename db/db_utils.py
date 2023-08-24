import sqlite3

def update(cursor, tabela, coluna, onde, valor):
    cursor.execute(f"UPDATE {tabela} SET {coluna} = '{valor}' WHERE id = {onde}")


def delete(cursor, tabela, onde):
    cursor.execute(f"DELETE FROM {tabela} WHERE id = {onde}")

def select(cursor, tabela, onde, valor):
    cursor.execute(f"SELECT * FROM {tabela} WHERE {onde} > {valor}")
    print(cursor.fetchall())

def executemany(cursor, tabela, colunas, items_tabela):
    interrogacao = ''
    for valores in colunas: 
        if valores ==  colunas[len(colunas) -1]:
            interrogacao += '?'
        else:
            interrogacao += '?, '
    cursor.executemany(f"""
    INSERT INTO {tabela} {colunas}
    VALUES ({interrogacao});
    """, items_tabela)



