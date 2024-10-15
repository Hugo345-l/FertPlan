# Importação dos módulos
import os
import oracledb
import pandas as pd

# Função para conectar ao banco de dados
def conectar_bd():
    try:
        conn = oracledb.connect(user='rm560688', password="120997", dsn='oracle.fiap.com.br:1521/ORCL')
        inst_cadastro = conn.cursor()
        inst_consulta = conn.cursor()
        inst_alteracao = conn.cursor()
        inst_exclusao = conn.cursor()
        return conn, inst_cadastro, inst_consulta, inst_alteracao, inst_exclusao
    except Exception as e:
        print("Erro ao conectar ao banco de dados: ", e)
        return None, None, None, None, None

# Exemplo de uso da função conectar_bd em outras funcionalidades
if __name__ == "__main__":
    conn, inst_cadastro, inst_consulta, inst_alteracao, inst_exclusao = conectar_bd()
    if conn:
        print("Conexão bem-sucedida!")
    else:
        print("Falha na conexão com o banco de dados.")