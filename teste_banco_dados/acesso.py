import pyodbc

aux = 177

# String de conexão com o banco de dados
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ts.daraujo.local;'
                      'Database=CVRBI02;'
                      'UID=gsv.novoacesso;'
                      'PWD=ESgsvxx11*')

# Criar um objeto cursor
cursor = conn.cursor()

# Comando SQL a executar, usando um placeholder (?) para o valor
cursor.execute('SELECT * FROM Planta WHERE clientes_codigo = ?', aux)

# Obter os nomes das colunas
columns = [column[0] for column in cursor.description]
print("Nomes das colunas:", columns)

# Buscar todos os resultados
for row in cursor:
    print(row)

conn.close()
