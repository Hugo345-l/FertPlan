import oracledb
from conexao_bd_fertplan import conectar_bd
import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def aguardar_usuario():
    input("Pressione Enter para continuar...")

def alterar_agricultor():
    conn, cursor, _, _, _ = conectar_bd()
    try:
        limpa_tela()
        while True:
            print("---- Alteração de Agricultor ----")
            cpf = input("Digite o CPF do Agricultor que deseja alterar (ou digite 'x' para cancelar): ")
            if cpf.lower() == 'x':
                return
            if not cpf.isdigit() or len(cpf) != 11:
                print("CPF inválido. Deve conter exatamente 11 dígitos.")
                aguardar_usuario()
                continue

            # Verifica se o agricultor existe
            query_verifica_agricultor = "SELECT COUNT(*) FROM FP_AGRICULTOR WHERE cpf = :cpf"
            cursor.execute(query_verifica_agricultor, cpf=cpf)
            (agricultor_existe,) = cursor.fetchone()
            
            if agricultor_existe == 0:
                print("Agricultor não encontrado. Verifique o CPF e tente novamente.")
                aguardar_usuario()
                continue

            # Permite que o usuário atualize os dados
            nome = input("Novo Nome (ou deixe em branco para não alterar): ").strip()
            email = input("Novo E-mail (ou deixe em branco para não alterar): ").strip()
            telefone = input("Novo Telefone (ou deixe em branco para não alterar): ").strip()

            campos_atualizar = {}
            if nome:
                campos_atualizar['nome'] = nome
            if email:
                campos_atualizar['email'] = email
            if telefone:
                campos_atualizar['telefone'] = telefone

            if not campos_atualizar:
                print("Nenhuma alteração realizada.")
                aguardar_usuario()
                continue

            try:
                query_update = "UPDATE FP_AGRICULTOR SET "
                query_update += ", ".join([f"{campo} = :{campo}" for campo in campos_atualizar])
                query_update += " WHERE cpf = :cpf"
                campos_atualizar['cpf'] = cpf
                cursor.execute(query_update, **campos_atualizar)
                conn.commit()
                print("Dados do agricultor atualizados com sucesso!")
                break
            except oracledb.DatabaseError as db_err:
                print(f"Erro ao atualizar agricultor: {db_err}")
                aguardar_usuario()
                continue
    except Exception as e:
        print(f"Erro ao alterar agricultor: {e}")
        aguardar_usuario()
    finally:
        print("Alteração feita com sucesso!")
        if conn:
            conn.close()

def alterar_propriedade():
    conn, cursor, _, _, _ = conectar_bd()
    try:
        limpa_tela()
        while True:
            print("---- Alteração de Propriedade ----")
            propriedade_id = input("Digite o ID da Propriedade que deseja alterar (ou digite 'x' para cancelar): ")
            if propriedade_id.lower() == 'x':
                return
            if not propriedade_id.isdigit():
                print("ID da propriedade inválido. Deve ser um valor numérico.")
                aguardar_usuario()
                continue

            # Verifica se a propriedade existe
            query_verifica_propriedade = "SELECT COUNT(*) FROM FP_PROPRIEDADE WHERE propriedade_id = :propriedade_id"
            cursor.execute(query_verifica_propriedade, propriedade_id=propriedade_id)
            (propriedade_existe,) = cursor.fetchone()
            
            if propriedade_existe == 0:
                print("Propriedade não encontrada. Verifique o ID e tente novamente.")
                aguardar_usuario()
                continue

            # Permite que o usuário atualize os dados
            nome = input("Novo Nome da Propriedade (ou deixe em branco para não alterar): ").strip()
            localizacao = input("Nova Localização (Estado) (ou deixe em branco para não alterar): ").strip()
            area_total = input("Nova Área Total (ou deixe em branco para não alterar): ").strip()

            campos_atualizar = {}
            if nome:
                campos_atualizar['nome'] = nome
            if localizacao:
                campos_atualizar['localizacao'] = localizacao
            if area_total:
                try:
                    area_total = float(area_total)
                    campos_atualizar['area_total'] = area_total
                except ValueError:
                    print("Área total inválida. Deve ser um valor numérico.")
                    aguardar_usuario()
                    continue

            if not campos_atualizar:
                print("Nenhuma alteração realizada.")
                aguardar_usuario()
                continue

            try:
                query_update = "UPDATE FP_PROPRIEDADE SET "
                query_update += ", ".join([f"{campo} = :{campo}" for campo in campos_atualizar])
                query_update += " WHERE propriedade_id = :propriedade_id"
                campos_atualizar['propriedade_id'] = propriedade_id
                cursor.execute(query_update, **campos_atualizar)
                conn.commit()
                print("Dados da propriedade atualizados com sucesso!")
                break
            except oracledb.DatabaseError as db_err:
                print(f"Erro ao atualizar propriedade: {db_err}")
                aguardar_usuario()
                continue
    except Exception as e:
        print(f"Erro ao alterar propriedade: {e}")
        aguardar_usuario()
    finally:
        print("Alteração feita com sucesso!")
        if conn:
            conn.close()

def alterar_plantacao():
    conn, cursor, _, _, _ = conectar_bd()
    try:
        limpa_tela()
        while True:
            print("---- Alteração de Plantação ----")
            plantacao_id = input("Digite o ID da Plantação que deseja alterar (ou digite 'x' para cancelar): ")
            if plantacao_id.lower() == 'x':
                return
            if not plantacao_id.isdigit():
                print("ID da plantação inválido. Deve ser um valor numérico.")
                aguardar_usuario()
                continue

            # Verifica se a plantação existe
            query_verifica_plantacao = "SELECT COUNT(*) FROM FP_PLANTACAO WHERE plantacao_id = :plantacao_id"
            cursor.execute(query_verifica_plantacao, plantacao_id=plantacao_id)
            (plantacao_existe,) = cursor.fetchone()
            
            if plantacao_existe == 0:
                print("Plantação não encontrada. Verifique o ID e tente novamente.")
                aguardar_usuario()
                continue

            # Permite que o usuário atualize os dados
            area_cultivo = input("Nova Área de Cultivo (ou deixe em branco para não alterar): ").strip()
            data_plantio = input("Nova Data de Plantio (formato: DD/MM/AAAA) (ou deixe em branco para não alterar): ").strip()

            campos_atualizar = {}
            if area_cultivo:
                try:
                    area_cultivo = float(area_cultivo)
                    campos_atualizar['area_cultivo'] = area_cultivo
                except ValueError:
                    print("Área de cultivo inválida. Deve ser um valor numérico.")
                    aguardar_usuario()
                    continue
            if data_plantio:
                try:
                    import pandas as pd
                    data_plantio = pd.to_datetime(data_plantio, format="%d/%m/%Y")
                    campos_atualizar['data_plantio'] = data_plantio
                except ValueError:
                    print("Data de plantio inválida. Use o formato DD/MM/AAAA.")
                    aguardar_usuario()
                    continue

            if not campos_atualizar:
                print("Nenhuma alteração realizada.")
                aguardar_usuario()
                continue

            try:
                query_update = "UPDATE FP_PLANTACAO SET "
                query_update += ", ".join([f"{campo} = :{campo}" for campo in campos_atualizar])
                query_update += " WHERE plantacao_id = :plantacao_id"
                campos_atualizar['plantacao_id'] = plantacao_id
                cursor.execute(query_update, **campos_atualizar)
                conn.commit()
                print("Dados da plantação atualizados com sucesso!")
                break
            except oracledb.DatabaseError as db_err:
                print(f"Erro ao atualizar plantação: {db_err}")
                aguardar_usuario()
                continue
    except Exception as e:
        print(f"Erro ao alterar plantação: {e}")
        aguardar_usuario()
    finally:
        print("Alteração feita com sucesso!")
        if conn:
            conn.close()

# Testa as funções
def alterar_agricultor_propriedade_plantacao():
    while True:
        limpa_tela()
        print("---- Sistema de Alteração ----")
        print("1. Alterar Agricultor")
        print("2. Alterar Propriedade")
        print("3. Alterar Plantação")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            alterar_agricultor()
        elif opcao == '2':
            alterar_propriedade()
        elif opcao == '3':
            alterar_plantacao()
        elif opcao == '4':
            break
        else:
            print("Opção inválida!")
