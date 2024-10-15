import oracledb
from conexao_bd_fertplan import conectar_bd
import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def aguardar_usuario():
    input("Pressione Enter para continuar...")

def remover_agricultor():
    conn, cursor, _, _, _ = conectar_bd()
    try:
        limpa_tela()
        while True:
            print("---- Remoção de Agricultor ----")
            cpf = input("Digite o CPF do Agricultor que deseja remover (ou digite 'x' para cancelar): ")
            if cpf.lower() == 'x':
                return
            if not cpf.isdigit() or len(cpf) != 11:
                print("CPF inválido. Deve conter exatamente 11 dígitos.")
                aguardar_usuario()
                continue

            try:
                # Verifica se o agricultor possui propriedades ou plantações
                query_verifica_dependencias = """
                    SELECT COUNT(*) 
                    FROM FP_PROPRIEDADE 
                    WHERE agricultor_id = (SELECT agricultor_id FROM FP_AGRICULTOR WHERE cpf = :cpf)
                """
                cursor.execute(query_verifica_dependencias, cpf=cpf)
                (propriedades,) = cursor.fetchone()
                
                if propriedades > 0:
                    print("Este agricultor possui propriedades cadastradas. Remova-as primeiro.")
                    aguardar_usuario()
                    continue

                # Remove o agricultor
                query_remover = "DELETE FROM FP_AGRICULTOR WHERE cpf = :cpf"
                cursor.execute(query_remover, cpf=cpf)
                conn.commit()
                print("Agricultor removido com sucesso!")
                break
            except oracledb.DatabaseError as db_err:
                print(f"Erro ao remover agricultor: {db_err}")
                aguardar_usuario()
                continue
    except Exception as e:
        print(f"Erro ao remover agricultor: {e}")
        aguardar_usuario()
    finally:
        print(f"Remoção concluída com sucesso!")
        if conn:
            conn.close()

def remover_propriedade():
    conn, cursor, _, _, _ = conectar_bd()
    try:
        limpa_tela()
        while True:
            print("---- Remoção de Propriedade ----")
            propriedade_id = input("Digite o ID da Propriedade que deseja remover (ou digite 'x' para cancelar): ")
            if propriedade_id.lower() == 'x':
                return
            if not propriedade_id.isdigit():
                print("ID da propriedade inválido. Deve ser um valor numérico.")
                aguardar_usuario()
                continue

            try:
                # Verifica se a propriedade possui plantações
                query_verifica_dependencias = """
                    SELECT COUNT(*) 
                    FROM FP_PLANTACAO 
                    WHERE propriedade_id = :propriedade_id
                """
                cursor.execute(query_verifica_dependencias, propriedade_id=propriedade_id)
                (plantacoes,) = cursor.fetchone()

                if plantacoes > 0:
                    print("Esta propriedade possui plantações cadastradas. Remova-as primeiro.")
                    aguardar_usuario()
                    continue

                # Remove a propriedade
                query_remover = "DELETE FROM FP_PROPRIEDADE WHERE propriedade_id = :propriedade_id"
                cursor.execute(query_remover, propriedade_id=propriedade_id)
                conn.commit()
                print("Propriedade removida com sucesso!")
                break
            except oracledb.DatabaseError as db_err:
                print(f"Erro ao remover propriedade: {db_err}")
                aguardar_usuario()
                continue
    except Exception as e:
        print(f"Erro ao remover propriedade: {e}")
        aguardar_usuario()
    finally:
        print(f"Remoção concluída com sucesso!")
        if conn:
            conn.close()

def remover_plantacao():
    conn, cursor, _, _, _ = conectar_bd()
    try:
        limpa_tela()
        while True:
            print("---- Remoção de Plantação ----")
            plantacao_id = input("Digite o ID da Plantação que deseja remover (ou digite 'x' para cancelar): ")
            if plantacao_id.lower() == 'x':
                return
            if not plantacao_id.isdigit():
                print("ID da plantação inválido. Deve ser um valor numérico.")
                aguardar_usuario()
                continue

            try:
                # Remove a plantação
                query_remover = "DELETE FROM FP_PLANTACAO WHERE plantacao_id = :plantacao_id"
                cursor.execute(query_remover, plantacao_id=plantacao_id)
                conn.commit()
                print("Plantação removida com sucesso!")
                break
            except oracledb.DatabaseError as db_err:
                print(f"Erro ao remover plantação: {db_err}")
                aguardar_usuario()
                continue
    except Exception as e:
        print(f"Erro ao remover plantação: {e}")
        aguardar_usuario()
    finally:
        print(f"Remoção concluída com sucesso!")
        if conn:
            conn.close()

def apagar_agricultor_propriedade_plantacao():
    while True:
        limpa_tela()
        print("---- Sistema de Remoção ----")
        print("1. Remover Agricultor")
        print("2. Remover Propriedade")
        print("3. Remover Plantação")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            remover_agricultor()
        elif opcao == '2':
            remover_propriedade()
        elif opcao == '3':
            remover_plantacao()
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")
            aguardar_usuario()
        break
