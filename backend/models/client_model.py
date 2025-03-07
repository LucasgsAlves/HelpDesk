import mysql.connector
from database.db_connection import create_connection, close_connection
from helpers.helpers import space_remover, convert_lowercase, convert_uppercase, standardize_text

def add_clients(nome, email, telefone, endereco):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()

            nome = standardize_text(nome)
            email = convert_lowercase(email)
            telefone = space_remover(telefone)
            endereco = convert_uppercase(endereco)

            sql = ('INSERT INTO clientes (nome, email, telefone, endereco) VALUES (%s, %s, %s, %s)')
            values = (nome, email, telefone, endereco)

            cursor.execute(sql, values)
            connection.commit()
            print('✅ Cliente cadastrado com sucesso!')
        except mysql.connector.Error as err:
            print(f'❌ Erro ao cadastrar cliente: {err}')
        finally:
            close_connection(connection)
    else:
        print('❌ Erro ao conectar ao Banco de Dados')

def update_clients(id, novo_nome, novo_email, novo_telefone, novo_endereco):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
        
            novo_nome = standardize_text(novo_nome)
            novo_email = convert_lowercase(novo_email)
            novo_telefone = space_remover(novo_telefone)
            novo_endereco = convert_uppercase(novo_endereco)
            
            sql = "UPDATE clientes SET nome = %s, email = %s, telefone = %s, endereco = %s WHERE id = %s"
            valores = (novo_nome, novo_email, novo_telefone, novo_endereco, id)
            
            cursor.execute(sql, valores)
            connection.commit()
            print('✅ Cliente atualizado com sucesso!')
        
        except mysql.connector.Error as err:
            print(f'❌ Erro ao atualizar cliente: {err}')
        finally:
            close_connection(connection)
    else:
        print('❌ Erro ao conectar ao Banco de Dados')

def list_clients():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            sql = "SELECT * FROM clientes"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            print(result)
            return result
        except mysql.connector.Error as err:
            print(f'❌ Erro ao listar cliente: {err}')
        finally:
            close_connection(connection)
    else:
        print('❌ Erro ao conectar ao Banco de Dados')

def delete_clients(id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            sql = "DELETE FROM clientes WHERE id = %s"
            values = (id,)
            
            cursor.execute(sql, values)
            connection.commit()
            print('✅ Cliente removido com sucesso!')
        except mysql.connector.Error as err:
            print(f'❌ Erro ao remover cliente: {err}')
        finally:
            close_connection(connection)
    else:
        print('❌ Erro ao conectar ao Banco de Dados')