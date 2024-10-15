import json
import oracledb
from conexao_bd_fertplan import conectar_bd

def listar_agricultores_propriedades_plantacoes():
    conn, cursor, _, _, _ = conectar_bd()
    try:
        # Consulta os dados das tabelas
        query_agricultores = "SELECT nome, email, telefone, cpf FROM FP_AGRICULTOR"
        cursor.execute(query_agricultores)
        agricultores = cursor.fetchall()

        query_propriedades = """
            SELECT p.propriedade_id, p.nome, p.localizacao, p.area_total, a.cpf 
            FROM FP_PROPRIEDADE p 
            JOIN FP_AGRICULTOR a ON p.agricultor_id = a.agricultor_id
        """
        cursor.execute(query_propriedades)
        propriedades = cursor.fetchall()

        query_plantacoes = """
            SELECT plantacao_id, propriedade_id, cultura_id, area_cultivo, solo_id, data_plantio 
            FROM FP_PLANTACAO
        """
        cursor.execute(query_plantacoes)
        plantacoes = cursor.fetchall()

        # Estrutura dos dados para exportação
        dados = {
            "agricultores": [
                {"nome": nome, "email": email, "telefone": telefone, "cpf": cpf}
                for nome, email, telefone, cpf in agricultores
            ],
            "propriedades": [
                {"propriedade_id": propriedade_id, "nome": nome, "localizacao": localizacao, 
                 "area_total": area_total, "cpf_agricultor": cpf}
                for propriedade_id, nome, localizacao, area_total, cpf in propriedades
            ],
            "plantacoes": [
                {"plantacao_id": plantacao_id, "propriedade_id": propriedade_id, "cultura_id": cultura_id, 
                 "area_cultivo": area_cultivo, "solo_id": solo_id, "data_plantio": data_plantio.strftime("%d/%m/%Y")}
                for plantacao_id, propriedade_id, cultura_id, area_cultivo, solo_id, data_plantio in plantacoes
            ]
        }

        # Exporta para um arquivo JSON, garantindo utf - 8 para linguagem portuguesa.
        with open('dados_exportados.json', 'w', encoding='utf-8') as json_file:
            json.dump(dados, json_file, ensure_ascii=False, indent=4)

        print("Dados exportados com sucesso para 'dados_exportados.json'.")

    except oracledb.DatabaseError as e:
        print("Erro ao consultar o banco de dados:", e)
    except Exception as e:
        print("Erro ao exportar dados:", e)
    finally:
        if conn:
            conn.close()

# Testa a função
if __name__ == "__main__":
    listar_agricultores_propriedades_plantacoes()
