import mysql.connector
from database.db_connection import create_connection, close_connection
from helpers.helpers import space_remover, convert_lowercase, convert_uppercase, standardize_text

def open_ticket(cliente_id,titulo, descricao):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()

            titulo = convert_uppercase(titulo)
            descricao = convert_lowercase(descricao)

            sql = 'INSERT INTO chamados (cliente_id, titulo, descricao) VALUES (%s, %s, %s) '
            values = (cliente_id, titulo, descricao)

            cursor.execute(sql, values)
            connection.commit()
            print('✅ Chamado criado com sucesso!')

        except mysql.connector.Error as err:
            print(f'❌ Erro ao criar chamado: {err}')
        finally:
            close_connection(connection)
    else:
        print('❌ Erro ao conectar ao Banco de Dados')

def update_ticket(id, novo_titulo, nova_descricao, novo_status):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()

            novo_titulo = standardize_text(novo_titulo)
            nova_descricao = convert_lowercase(nova_descricao)
            novo_status = convert_lowercase(novo_status)

            sql = 'UPDATE chamados SET titulo = %s, descricao = %s, status = %s WHERE id = %s'
            values = (novo_titulo, nova_descricao, novo_status, id)
            cursor.execute(sql, values)

            connection.commit()
            print('✅ Chamado atualizado com sucesso!')
        except mysql.connector.Error as err:
            print(f'❌ Erro ao atualizar chamado: {err}')
        finally:
            close_connection(connection)
    else:
        print('❌ Erro ao conectar ao Banco de Dados')

def list_tickets():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM chamados')
            result = cursor.fetchall()
            cursor.close()
            print(result)
            return result
        except mysql.connector.Error as err:
            print(f'❌ Erro ao listar chamado: {err}')
        finally:
            close_connection(connection)
    else:
        print('❌ Erro ao conectar ao Banco de Dados')

def delete_ticket(id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            sql = "DELETE FROM chamados WHERE id = %s"
            values = (id,)
            
            cursor.execute(sql, values)
            connection.commit()
            print('✅ Chamado removido com sucesso!')
        except mysql.connector.Error as err:
            print(f'❌ Erro ao remover cliente: {err}')
        finally:
            close_connection(connection)
    else:
        print('❌ Erro ao conectar ao Banco de Dados')
