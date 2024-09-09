import pyodbc

# String de conexão com o banco de dados
conn = pyodbc.connect('Driver={SQL Server};'
'Server=ts.daraujo.local;'
'Database=CVRBI02;'
'UID=gsv.novoacesso;'
'PWD=ESgsvxx11*')

# Criar um objeto cursor
cursor = conn.cursor()

# Comando SQL a executar
cursor.execute('SELECT * FROM Clientes')

# Buscar todos os resultados
for row in cursor:
    print(row)

conn.close()