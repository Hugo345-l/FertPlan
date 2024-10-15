# Importação dos módulos
import os
import oracledb
import pandas as pd
from conexao_bd_fertplan import conectar_bd

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def recomendar_fertilizantes():
    # Conexão com o banco de dados
    conn, _, _, _, _ = conectar_bd()
    
    # Limpa a tela para melhor visualização do menu
    limpa_tela()
    print("---- Recomendador de Fertilizantes ----")
    
    try:
        cursor = conn.cursor()
        
        # Solicita o CPF do agricultor para identificar as propriedades
        cpf = input("Informe o CPF do agricultor: ")
        
        # Consulta para obter as propriedades do agricultor com base no CPF
        query_propriedades = """
            SELECT propriedade_id, nome
            FROM FP_PROPRIEDADE p
            JOIN FP_AGRICULTOR a ON p.agricultor_id = a.agricultor_id
            WHERE a.cpf = :cpf
        """
        
        cursor.execute(query_propriedades, {'cpf': cpf})
        propriedades = cursor.fetchall()
        
        if not propriedades:
            print("Nenhuma propriedade encontrada para o CPF informado. Verifique os dados e tente novamente.")
            return
        
        print("\nPropriedades encontradas:")
        for prop in propriedades:
            print(f"ID: {prop[0]}, Nome: {prop[1]}")
        
        propriedade_id = input("Informe o ID da propriedade desejada: ")
        
        # Consulta para obter as plantações da propriedade selecionada
        query_plantacoes = """
            SELECT plantacao_id, cultura_id, area_cultivo
            FROM FP_PLANTACAO
            WHERE propriedade_id = :propriedade_id
        """
        
        cursor.execute(query_plantacoes, {'propriedade_id': propriedade_id})
        plantacoes = cursor.fetchall()
        
        if not plantacoes:
            print("Nenhuma plantação encontrada para a propriedade selecionada.")
            return
        
        print("\nPlantações encontradas:")
        for plant in plantacoes:
            print(f"ID: {plant[0]}, Cultura ID: {plant[1]}, Área de Cultivo: {plant[2]} hectares")
        
        plantacao_id = input("Informe o ID da plantação desejada: ")
        
        # Consulta as informações da plantação, cultura e tipo de solo
        query = """
            SELECT c.nome AS cultura, s.tipo_solo AS solo
            FROM FP_PLANTACAO p
            JOIN FP_CULTURA c ON p.cultura_id = c.cultura_id
            JOIN FP_SOLO s ON p.solo_id = s.solo_id
            WHERE p.plantacao_id = :plantacao_id
        """
        
        cursor.execute(query, {'plantacao_id': plantacao_id})
        resultado = cursor.fetchone()
        
        if resultado:
            cultura, solo = resultado
            print(f"\nCultura: {cultura}, Tipo de Solo: {solo}")
            
            # Consulta recomendação de fertilizante com base na cultura e no tipo de solo
            query_fertilizante = """
                SELECT f.nome, f.concentracao, f.fornecedor, f.preco_kg_local, csf.recomendacao
                FROM FP_CULTURA_SOLO_FERTILIZANTE csf
                JOIN FP_FERTILIZANTE f ON csf.fertilizante_id = f.fertilizante_id
                WHERE csf.cultura_id = (
                    SELECT cultura_id FROM FP_CULTURA WHERE nome = :cultura
                )
                AND csf.solo_id = (
                    SELECT solo_id FROM FP_SOLO WHERE tipo_solo = :solo
                )
            """
            
            cursor.execute(query_fertilizante, {'cultura': cultura, 'solo': solo})
            fertilizantes = cursor.fetchall()
            
            if fertilizantes:
                print("\nRecomendações de Fertilizantes:")
                for f in fertilizantes:
                    nome, concentracao, fornecedor, preco_kg_local, recomendacao = f
                    print(f"Nome: {nome}, Concentracao: {concentracao}, Fornecedor: {fornecedor}, Preço (Local): R$ {preco_kg_local}, Recomendação: {recomendacao}")
                    
                    # Inserir recomendação na base de dados
                    insert_recomendacao = """
                        INSERT INTO FP_CULTURA_SOLO_FERTILIZANTE (cultura_id, solo_id, fertilizante_id, recomendacao)
                        VALUES (
                            (SELECT cultura_id FROM FP_CULTURA WHERE nome = :cultura),
                            (SELECT solo_id FROM FP_SOLO WHERE tipo_solo = :solo),
                            (SELECT fertilizante_id FROM FP_FERTILIZANTE WHERE nome = :nome),
                            :recomendacao
                        )
                    """
                    cursor.execute(insert_recomendacao, {'cultura': cultura, 'solo': solo, 'nome': nome, 'recomendacao': recomendacao})
                    conn.commit()
            else:
                print("Nenhuma recomendação encontrada para a combinação de cultura e tipo de solo informados.")
        else:
            print("Plantação ou propriedade não encontrada. Verifique os IDs informados.")
        
    except oracledb.Error as e:
        print(f"Erro ao realizar consulta: {e}")
    finally:
        if conn:
            conn.close()
        input("\nPressione Enter para continuar...")