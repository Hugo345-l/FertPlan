import os 
from conexao_bd_fertplan import conectar_bd
import oracledb

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def aguardar_usuario():
    input("Pressione Enter para continuar...")

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) in [10, 11]

def validar_email(email):
    return "@" in email

def cadastrar_agricultor():
    conn, inst_cadastro, _, _, _ = conectar_bd()
    
    try:
        limpa_tela()
        while True:
            print("---- Cadastro de Agricultor ----")
            
            nome_completo = input("Nome Completo (ou digite 'x' para cancelar): ")
            if nome_completo.lower() == 'x':
                return
            if not nome_completo.strip():
                print("Nome completo é obrigatório.")
                aguardar_usuario()
                continue
            
            email = input("E-mail (ou digite 'x' para cancelar): ")
            if email.lower() == 'x':
                return
            telefone = input("Telefone (Ex: DDD + Número, ex: 11912345678) (ou digite 'x' para cancelar): ")
            if telefone.lower() == 'x':
                return
            cpf = input("CPF (somente números, 11 dígitos) (ou digite 'x' para cancelar): ")
            if cpf.lower() == 'x':
                return
            
            if not email.strip() and not telefone.strip():
                print("É necessário informar pelo menos um contato (e-mail ou telefone).")
                aguardar_usuario()
                continue
            
            if email and not validar_email(email):
                print("E-mail inválido.")
                aguardar_usuario()
                continue
            
            if telefone and not validar_telefone(telefone):
                print("Telefone inválido. Deve conter 10 ou 11 dígitos, incluindo o DDD. Exemplo: 11912345678.")
                aguardar_usuario()
                continue
            
            if not validar_cpf(cpf):
                print("CPF inválido. Deve conter exatamente 11 dígitos.")
                aguardar_usuario()
                continue
            
            try:
                query_verifica_cpf = "SELECT COUNT(*) FROM FP_AGRICULTOR WHERE cpf = :cpf"
                inst_cadastro.execute(query_verifica_cpf, cpf=cpf)
                (cpf_existe,) = inst_cadastro.fetchone()
                if cpf_existe > 0:
                    print("CPF já cadastrado. Utilize um CPF diferente.")
                    aguardar_usuario()
                    continue
            except oracledb.DatabaseError as db_err:
                print(f"Erro ao verificar CPF no banco de dados: {db_err}")
                aguardar_usuario()
                continue
            
            try:
                query = """
                    INSERT INTO FP_AGRICULTOR (nome, email, telefone, cpf)
                    VALUES (:nome_completo, :email, :telefone, :cpf)
                """
                inst_cadastro.execute(query, nome_completo=nome_completo, email=email, telefone=telefone, cpf=cpf)
                conn.commit()
                print("Agricultor cadastrado com sucesso!")
                break
            except oracledb.DatabaseError as db_err:
                print(f"Erro de banco de dados ao cadastrar agricultor: {db_err}")
                aguardar_usuario()
    except Exception as e:
        print(f"Erro ao cadastrar agricultor: {e}")
        aguardar_usuario()
    finally:
        if conn:
            conn.close()
