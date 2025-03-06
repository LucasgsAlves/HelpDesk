import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def create_connection():
    try:
        connection = mysql.connector.connect(
            host = os.getenv('DB_HOST'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            database = os.getenv('DB_NAME')
        )
        print(f'✅ Conexão bem sucedida!')
        return connection
    except mysql.connector.Error as err:
        print(f'❌ Erro ao conectar ao Banco de Dados: {err}')
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print('✅ Conexão encerrada com sucesso!')