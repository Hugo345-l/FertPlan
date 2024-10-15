import os 
import oracledb
from conexao_bd_fertplan import conectar_bd
from cadastrar_agricultor import cadastrar_agricultor

# Função para limpar a tela
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cadastrar_propriedade():
    def aguardar_usuario():
        input("Pressione Enter para continuar...")
    conn, inst_cadastro, _, _, _ = conectar_bd()
    limpa_tela()
    while True:
        try:
            print("---- Cadastro de Propriedade ----")
            
            # Coleta de informações da propriedade
            cpf_agricultor = input("CPF do Agricultor (somente números, 11 dígitos) (ou digite 'x' para cancelar): ")
            if cpf_agricultor.lower() == 'x':
                return
            if not cpf_agricultor.isdigit() or len(cpf_agricultor) != 11:
                print("CPF do Agricultor inválido. Deve conter exatamente 11 dígitos.")
                aguardar_usuario()
                continue
            
            # Verificação se o agricultor existe na base
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
            
            nome_propriedade = input("Nome da Propriedade (ou digite 'x' para cancelar): ")
            if nome_propriedade.lower() == 'x':
                return
            if not nome_propriedade.strip():
                print("Nome da propriedade é obrigatório.")
                aguardar_usuario()
                continue
            
            # Seleção da localização (estado)
            estados = [
                "1 - AC", "2 - AL", "3 - AP", "4 - AM", "5 - BA", "6 - CE", "7 - DF", "8 - ES", "9 - GO",
                "10 - MA", "11 - MT", "12 - MS", "13 - MG", "14 - PA", "15 - PB", "16 - PR", "17 - PE", "18 - PI",
                "19 - RJ", "20 - RN", "21 - RS", "22 - RO", "23 - RR", "24 - SC", "25 - SP", "26 - SE", "27 - TO"
            ]
            for estado in estados:
                print(estado)
            print()  # Linha em branco para separar visualmente
            estado_numero = input("Digite o número correspondente ao Estado (ou digite 'x' para cancelar): ")
            if estado_numero.lower() == 'x':
                return
            if not estado_numero.isdigit() or int(estado_numero) not in range(1, 28):
                print("Opção inválida. Escolha um número de 1 a 27.")
                aguardar_usuario()
                continue
            localizacao = estados[int(estado_numero) - 1].split(" - ")[1]
            
            area_total = input("Área Total em hectares (ou digite 'x' para cancelar): ")
            if area_total.lower() == 'x':
                return
            try:
                area_total = float(area_total)
                if area_total <= 0:
                    print("Área total deve ser um valor positivo.")
                    aguardar_usuario()
                    continue
            except ValueError:
                print("Área total inválida. Deve ser um valor numérico.")
                aguardar_usuario()
                continue
            
            # Inserção no banco de dados
            try:
                query = """
                    INSERT INTO FP_PROPRIEDADE (agricultor_id, nome, localizacao, area_total)
                    VALUES ((SELECT agricultor_id FROM FP_AGRICULTOR WHERE cpf = :cpf), :nome_propriedade, :localizacao, :area_total)
                """
                inst_cadastro.execute(query, cpf=cpf_agricultor, nome_propriedade=nome_propriedade, localizacao=localizacao, area_total=area_total)
                conn.commit()
                print("Propriedade cadastrada com sucesso!")
                break
            except oracledb.DatabaseError as db_err:
                print("Erro de banco de dados ao cadastrar propriedade: ", db_err)
                aguardar_usuario()
        except Exception as e:
            print("Erro ao cadastrar propriedade: ", e)
            aguardar_usuario()
    aguardar_usuario()