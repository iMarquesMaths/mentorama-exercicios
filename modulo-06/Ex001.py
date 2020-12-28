import sqlite3

#Conecta o banco de dados com a memoria do pc (reinicia quando recarrega)
database = sqlite3.connect(':memory:')

#Conecta o banco de dados criando um arquivo no pc (da conflito caso o banco ja exista)
#database = sqlite3.connect('teste.db')

#define um cursor para interagir com o banco de dados
cursor = database.cursor()

#função para criação da tabela funcionarios
def create_table_funcionarios:
    sql = """
    CREATE TABLE IF NOT EXISTS employees (
    idEmployees INTEGER NOT NULL PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    birthdate TEXT,
    cpf INTEGER,
    rg INTEGER,
    address TEXT,
    cep INTEGER,
    city TEXT,
    phoneNumber INTEGER,
    idDepartament INTEGER,
    occupation TEXT,
    function TEXT,
    salary FLOAT)
    """
    cursor.execute(sql)
    database.commit()