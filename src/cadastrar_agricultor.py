# Função para cadastrar um agricultor
import os 
from conexao_bd_fertplan import conectar_bd
import oracledb

# Função para limpar a tela
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_agricultor():
    def aguardar_usuario():
        input("Pressione Enter para continuar...")
     # Conecta ao banco de dados e obtem o cursor necessário
    conn, inst_cadastro, _, _, _ = conectar_bd()
    limpa_tela()
    while True:
        try:
            print("---- Cadastro de Agricultor ----")
            
            # Coleta de informações do agricultor
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
            
            # Validação dos dados coletados
            if not email.strip() and not telefone.strip():
                print("É necessário informar pelo menos um contato (e-mail ou telefone).")
                aguardar_usuario()
                continue
            if email and "@" not in email:
                print("E-mail inválido.")
                aguardar_usuario()
                continue
            if telefone and (not telefone.isdigit() or len(telefone) not in [10, 11]):
                print("Telefone inválido. Deve conter 10 ou 11 dígitos, incluindo o DDD. Exemplo: 11912345678.")
                aguardar_usuario()
                continue
            if not cpf.isdigit() or len(cpf) != 11:
                print("CPF inválido. Deve conter exatamente 11 dígitos.")
                aguardar_usuario()
                continue
            
            # Verificação se o CPF já existe na base
            try:
                query_verifica_cpf = "SELECT COUNT(*) FROM FP_AGRICULTOR WHERE cpf = :cpf"
                inst_cadastro.execute(query_verifica_cpf, cpf=cpf)
                (cpf_existe,) = inst_cadastro.fetchone()
                if cpf_existe > 0:
                    print("CPF já cadastrado. Utilize um CPF diferente.")
                    aguardar_usuario()
                    continue
            except oracledb.DatabaseError as db_err:
                print("Erro ao verificar CPF no banco de dados: ", db_err)
                aguardar_usuario()
                continue
            
            # Inserção no banco de dados
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
                print("Erro de banco de dados ao cadastrar agricultor: ", db_err)
                aguardar_usuario()
        except Exception as e:
            print("Erro ao cadastrar agricultor: ", e)
            aguardar_usuario()
    aguardar_usuario()