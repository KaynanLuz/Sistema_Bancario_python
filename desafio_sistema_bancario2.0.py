from datetime import datetime

def menu():
    menu_texto = """\n\n ------------Bem vindo ao Banco Nampão Bank---------------

[1] Depositar
[2] Sacar 
[3] Extrato
[4] Cadastro Novo usuário
[5] Criar Conta Corrente
[0] Sair

=> """
    return menu_texto

class variaveis_sistema():
    valor_total_conta = 0
    limite_transacoes = 3
    comprovante = []
    limite_diario_saque = 1500  # Definindo um limite diário de saque padrão
    valor_sacado_hoje = 0 
    mascara_datahora_ptbr = "%d/%m/%Y %H:%M:%S"
    usuarios_list = []  # Lista de usuários
    contas_list = []    # Lista de contas
    numero_conta_sequencial = 1  # Número da conta começa em 1

def executar_sistema_banco():
    numero_saques = 0  # Adiciona a contagem de saques

    while True:
        opcao = input(menu())

        if opcao == "1":
            if variaveis_sistema.limite_transacoes <= 0:
                print("\nLimite diário de transações excedido, volte amanhã!")
            else:
                valor_depositado = int(input("Deposite o valor desejado R$: "))
                variaveis_sistema.valor_total_conta, variaveis_sistema.comprovante = depositar(
                    variaveis_sistema.valor_total_conta, valor_depositado, variaveis_sistema.comprovante
                )
        
        elif opcao == "2":
            if variaveis_sistema.limite_transacoes <= 0:
                print("\nLimite diário de transações excedido, volte amanhã!")
            elif variaveis_sistema.valor_total_conta <= 0:
                print("\nSua conta está sem limite, faça um deposito!")
            else:
                valor_saque = int(input("Quanto deseja sacar? "))
                if variaveis_sistema.valor_sacado_hoje + valor_saque > variaveis_sistema.limite_diario_saque:
                    print(f"\nLimite diário de saque de R$ 1500 excedido. Você já sacou R$ {variaveis_sistema.valor_sacado_hoje:.2f} hoje.")
                else:
                    variaveis_sistema.valor_total_conta, variaveis_sistema.comprovante = saque(
                        saldo=variaveis_sistema.valor_total_conta, 
                        extrato=variaveis_sistema.comprovante, 
                        valor=valor_saque,
                        numero_saques=numero_saques
                    )

        elif opcao == "3":
            comprovante(variaveis_sistema.valor_total_conta, extrato=variaveis_sistema.comprovante)

        elif opcao == "4":
            cadastrar_usuario()  

        elif opcao == "5":
            criar_conta_corrente()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente!")     
        
    # Reseta o limite de transações e saque diário para o dia seguinte
    variaveis_sistema.limite_transacoes = 3  
    variaveis_sistema.valor_sacado_hoje = 0

def limite_transacoes_diarias():
    if variaveis_sistema.limite_transacoes == 0:
        print("\nLimite diário de transações excedido, volte amanhã!")
        return False
    variaveis_sistema.limite_transacoes -= 1 
    return True

def data_hora_transacao():
    return datetime.today()

def depositar(saldo, valor_depositado, comprovante, /):
    if not limite_transacoes_diarias():
        return saldo, comprovante

    if valor_depositado <= 0:
        print("\nValor inválido")
    else:
        saldo += valor_depositado
        data_hora = data_hora_transacao()
        comprovante.append(f"Depósito R$: {valor_depositado:.2f} | {data_hora.strftime(variaveis_sistema.mascara_datahora_ptbr)}")

        print(f"\n\nDepósito efetuado com sucesso! \n\nValor atual da sua Conta R$: {saldo:.2f} ")

    return saldo, comprovante

def comprovante(saldo, *, extrato):
    if variaveis_sistema.comprovante:
        print("\n----------- EXTRATO -----------")
        for transacao in variaveis_sistema.comprovante:
            print(transacao)
        print(f"\nSaldo atual na conta: R$ {variaveis_sistema.valor_total_conta:.2f}")
        print("-------------------------------")
    else:
        print("\nNão foram realizadas movimentações.")

def saque(*, saldo, extrato, valor, numero_saques):
    if not limite_transacoes_diarias():
        return saldo, extrato

    if saldo > 0:
        print(f"Valor atual da sua conta R$: {saldo:.2f}\n")

        if valor > saldo:
            print("\nNão foi possível realizar o saque, valor de saque maior do que contém na conta.")
            return saldo, extrato
        elif valor < 0:
            print("\nNão é possível fazer saques negativos!")
            return saldo, extrato
        elif valor == 0:
            print("\nNão é possível sacar 0 valores!") 
            return saldo, extrato
        elif numero_saques >= 3:  # Aqui podemos usar o limite fixo de saques
            print("\nLimite de saques diários atingido.")
            return saldo, extrato
        
        saldo -= valor
        variaveis_sistema.valor_sacado_hoje += valor

        data_hora = data_hora_transacao()  
        extrato.append(f"Saque    R$: {valor:.2f} | {data_hora.strftime(variaveis_sistema.mascara_datahora_ptbr)}")
        numero_saques += 1

        print(f"\nSaque efetuado com sucesso! \nValor atual da sua Conta R$: {saldo:.2f} ")

    else:      
        print(f"Saldo na conta insuficiente R$: {saldo:.2f}")

    return saldo, extrato

def cadastrar_usuario():
    print("\n--- Cadastro de novo usuário ---")
    nome = input("Digite o nome do usuário: ")
    dt_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF (somente números): ")
    
    cpf = ''.join(filter(str.isdigit, cpf))
    
    for usuario in variaveis_sistema.usuarios_list:
        if usuario["cpf"] == cpf:
            print("\nErro: CPF já cadastrado. Tente novamente.")
            return

    rua = input("Qual é sua rua: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Qual sua cidade: ")
    sigla = input("Sigla do estado: ")

    endereco = f"{rua}, {numero} – {bairro} – {cidade}/{sigla}"

    novo_usuario = {
        "nome": nome,
        "data_nascimento": dt_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    variaveis_sistema.usuarios_list.append(novo_usuario)

    print("\nUsuário cadastrado com sucesso!")

def criar_conta_corrente():
    print("\n--- Criação de Conta Corrente ---")
    
    cpf = input("Digite o CPF do usuário para vincular a conta (somente números): ")
    cpf = ''.join(filter(str.isdigit, cpf))

    usuario_encontrado = None
    for usuario in variaveis_sistema.usuarios_list:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("Erro: Usuário não encontrado. Cadastre o usuário primeiro.")
        return

    # Criação da conta
    numero_conta = variaveis_sistema.numero_conta_sequencial
    agencia = "0001"  # Agência fixa
    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario_encontrado
    }

    variaveis_sistema.contas_list.append(nova_conta)
    variaveis_sistema.numero_conta_sequencial += 1

    print(f"\nConta criada com sucesso!\nAgência: {agencia} | Número da Conta: {numero_conta}")

executar_sistema_banco()
