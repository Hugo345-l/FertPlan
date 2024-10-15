# Função para cadastrar um agricultor
import os 
import oracledb
from conexao_bd_fertplan import conectar_bd
from cadastrar_agricultor import cadastrar_agricultor
from cadastrar_propriedade import cadastrar_propriedade
import pandas as pd


# Função para limpar a tela
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def cadastrar_plantacao():
    def aguardar_usuario():
        input("Pressione Enter para continuar...")
    conn, inst_cadastro, _, _, _ = conectar_bd()
    limpa_tela()
    while True:
        try:
            print("---- Cadastro de Plantação ----")
            
            # Coleta do CPF do agricultor e verifica se existe
            cpf_agricultor = input("CPF do Agricultor (somente números, 11 dígitos) (ou digite 'x' para cancelar): ")
            if cpf_agricultor.lower() == 'x':
                return
            if not cpf_agricultor.isdigit() or len(cpf_agricultor) != 11:
                print("CPF do Agricultor inválido. Deve conter exatamente 11 dígitos.")
                aguardar_usuario()
                continue
            
            try:
                query_verifica_agricultor = "SELECT COUNT(*) FROM FP_AGRICULTOR WHERE cpf = :cpf"
                inst_cadastro.execute(query_verifica_agricultor, cpf=cpf_agricultor)
                (agricultor_existe,) = inst_cadastro.fetchone()
                if agricultor_existe == 0:
                    print("CPF do Agricultor não encontrado. Verifique e tente novamente ou pressione 'n' para cadastrar um novo agricultor.")
                    opcao = input("Digite 'n' para cadastrar um novo agricultor ou qualquer outra tecla para tentar novamente: ")
                    if opcao.lower() == 'n':
                        cadastrar_agricultor()
                    else:
                        aguardar_usuario()
                    continue
            except oracledb.DatabaseError as db_err:
                print("Erro ao verificar agricultor no banco de dados: ", db_err)
                aguardar_usuario()
                continue
            
            # Seleciona a propriedade
            query_busca_propriedades = "SELECT propriedade_id, nome FROM FP_PROPRIEDADE WHERE agricultor_id = (SELECT agricultor_id FROM FP_AGRICULTOR WHERE cpf = :cpf)"
            inst_cadastro.execute(query_busca_propriedades, cpf=cpf_agricultor)
            propriedades = inst_cadastro.fetchall()
            if not propriedades:
                print("Nenhuma propriedade encontrada para este agricultor. Pressione 'n' para cadastrar uma nova propriedade ou 'x' para sair.")
                opcao = input("Digite 'n' para cadastrar uma nova propriedade ou 'x' para sair: ")
                if opcao.lower() == 'n':
                    cadastrar_propriedade()
                else:
                    return
                continue
            
            print("Propriedades Disponíveis:")
            for idx, (prop_id, prop_nome) in enumerate(propriedades, start=1):
                print(f"{idx} - {prop_nome}")
            opcao_prop = input("Escolha o número da propriedade para cadastrar a plantação (ou digite 'x' para cancelar): ")
            if opcao_prop.lower() == 'x':
                return
            if not opcao_prop.isdigit() or int(opcao_prop) not in range(1, len(propriedades) + 1):
                print("Opção inválida.")
                aguardar_usuario()
                continue
            propriedade_id = propriedades[int(opcao_prop) - 1][0]
            
            # Seleção da cultura
            query_busca_culturas = "SELECT cultura_id, nome FROM FP_CULTURA"
            inst_cadastro.execute(query_busca_culturas)
            culturas = inst_cadastro.fetchall()
            print("Culturas Disponíveis:")
            for idx, (cult_id, cult_nome) in enumerate(culturas, start=1):
                print(f"{idx} - {cult_nome}")
            opcao_cultura = input("Escolha a cultura plantada (ou digite 'x' para cancelar): ")
            if opcao_cultura.lower() == 'x':
                return
            if not opcao_cultura.isdigit() or int(opcao_cultura) not in range(1, len(culturas) + 1):
                print("Opção inválida.")
                aguardar_usuario()
                continue
            cultura_id = culturas[int(opcao_cultura) - 1][0]
            
            area_cultivo = input("Área de Cultivo em hectares (ou digite 'x' para cancelar): ")
            if area_cultivo.lower() == 'x':
                return
            try:
                area_cultivo = float(area_cultivo)
                if area_cultivo <= 0:
                    print("Área de cultivo deve ser um valor positivo.")
                    aguardar_usuario()
                    continue
            except ValueError:
                print("Área de cultivo inválida. Deve ser um valor numérico.")
                aguardar_usuario()
                continue
            
            # Seleção do tipo de solo
            query_busca_solos = "SELECT solo_id, tipo_solo FROM FP_SOLO"
            inst_cadastro.execute(query_busca_solos)
            solos = inst_cadastro.fetchall()
            print("Tipos de Solo Disponíveis:")
            for idx, (solo_id, tipo_solo) in enumerate(solos, start=1):
                print(f"{idx} - {tipo_solo}")
            opcao_solo = input("Escolha o tipo de solo (ou digite 'x' para cancelar): ")
            if opcao_solo.lower() == 'x':
                return
            if not opcao_solo.isdigit() or int(opcao_solo) not in range(1, len(solos) + 1):
                print("Opção inválida.")
                aguardar_usuario()
                continue
            solo_id = solos[int(opcao_solo) - 1][0]
            
            data_plantio = input("Data de Plantio (formato: DD/MM/AAAA) (ou digite 'x' para cancelar): ")
            if data_plantio.lower() == 'x':
                return
            try:
                data_plantio = pd.to_datetime(data_plantio, format="%d/%m/%Y")
            except ValueError:
                print("Data de plantio inválida. Use o formato DD/MM/AAAA.")
                aguardar_usuario()
                continue
            
            # Inserção no banco de dados
            try:
                query = """
                    INSERT INTO FP_PLANTACAO (propriedade_id, cultura_id, area_cultivo, solo_id, data_plantio)
                    VALUES (:propriedade_id, :cultura_id, :area_cultivo, :solo_id, :data_plantio)
                """
                inst_cadastro.execute(query, propriedade_id=propriedade_id, cultura_id=cultura_id,
                                     area_cultivo=area_cultivo, solo_id=solo_id, data_plantio=data_plantio)
                conn.commit()
                print("Plantação cadastrada com sucesso!")
                break
            except oracledb.DatabaseError as db_err:
                print("Erro de banco de dados ao cadastrar plantação: ", db_err)
                aguardar_usuario()
        except Exception as e:
            print("Erro ao cadastrar plantação: ", e)
            aguardar_usuario()
    aguardar_usuario()
