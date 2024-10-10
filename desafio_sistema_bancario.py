# from datetime import datetime
# import time


# menu = """\n\n ------------Bem vindo ao Banco Nampão Bank---------------

# [1] Depositar
# [2] Sacar 
# [3] Extrato
# [0] Sair

# => """

# valor_deposito = 0;
# valor_saque = 0;
# total_conta = 0;
# limite_diario = 1500;
# comprovante = [];
# limite_transacoes = 4;
# mascara_datahora_ptbr = "%d/%m/%Y, %H:%M:%S"


# while True:

#     opcao = input(menu)

#     if opcao == "1":

#         if limite_transacoes == 0:
#             print("\nLimite diário de transações excedidas, volte amanhã!") 

#         else:
#             valor_deposito = int(input("Deposite o valor desejado R$: "))

#             if valor_deposito <= 0:
#                 print("\nValor Inválido!")
            
#             else:     
#                 total_conta += valor_deposito;  
#                 data_hora_transacao = datetime.today();  
#                 comprovante.append(f"Depósito: R$ {valor_deposito:.2f} | {data_hora_transacao.strftime(mascara_datahora_ptbr)}")
#                 time.sleep(1)
#                 limite_transacoes = limite_transacoes - 1

#                 print(f"\n\nDeposito efetuado com sucesso! \n\nValor atual da sua Conta R$: {total_conta:.2f} ")
        
#     elif opcao == "2":     

#         if limite_transacoes == 0:
#            print("Limite diário de transações excedidas, volte amanhã!") 
            
#         elif total_conta > 0:

#             print(f"Limite máximo de saque diário R$: {limite_diario:.2f}\n\n")

#             print(f"Valor atual da sua conta R$: {total_conta:.2f}\n\n")   
             
#             valor_saque = int(input("Quanto deseja sacar? "))

#             if valor_saque > total_conta:

#                 print("\nNão foi possivel realizar o saque, valor de saque maior do que contém na conta")

#             elif valor_saque > limite_diario:
#                 print("\nLimite diário máximo excedido!!!") 
            
#             elif valor_saque < 0:
#                 print("\nNão é possivel fazer saques negativos!")

#             elif valor_saque == 0:
#                 print("\nNão é possivel sacar 0 valores!")

#             else:
#                 total_conta -= valor_saque
#                 limite_diario -= valor_saque
#                 data_hora_transacao = datetime.today();
#                 comprovante.append(f"Saque:    R$ {valor_saque:.2f} | {data_hora_transacao.strftime(mascara_datahora_ptbr)}")
#                 time.sleep(1)
#                 limite_transacoes = limite_transacoes - 1

#                 print(f"\n\nSaque efetuado com sucesso! \n\nValor atual da sua Conta R$: {total_conta:.2f} ")
#                 print(f"\n\nValor disponivel para saque diário R$: {limite_diario:.2f} ")

#         else:      
#             print(f"Saldo na conta insuficiente R$: {total_conta:.2f}")    

#     elif opcao == "3":

#         if comprovante:
#             print("\n----------- EXTRATO -----------")
#             for transacao in comprovante:
#                 print(transacao)

#             print(f"\nSaldo atual na conta: R$ {total_conta:.2f}")
#             print("-------------------------------")
#         else:
#             print("\nNão foram realizadas movimentações.")
    
#     elif opcao == "0":
#         print("Saindo...")
#         break
    
#     else:
#         print("Opção inválida, tente novamente!")























#         def saque(* saldo, comprovante, limite_diario, valor_saque):
#     if not limite_transacoes_diarias():
#         return saldo, comprovante
    
#     elif saldo > 0:

#             limite_diario_saque()

#             print(f"Valor atual da sua conta R$: {saldo:.2f}\n\n")   
             
#             valor_saque = int(input("Quanto deseja sacar? "))

#             if valor_saque > saldo:

#                 print("\nNão foi possivel realizar o saque, valor de saque maior do que contém na conta")

#             elif limite_diario_saque()

#             elif valor_saque < 0:
#                 print("\nNão é possivel fazer saques negativos!")

#             elif valor_saque == 0:
#                 print("\nNão é possivel sacar 0 valores!") 

#             else:
#                 saldo -= valor_saque
#                 limite_diario_saque()
#                 data_hora_transacao()
#                 comprovante.append(f"Saque:    R$ {valor_saque:.2f} | {data_hora_transacao.strftime(variaveis_sistema.mascara_datahora_ptbr)}")
#                 time.sleep(1)
#                 limite_transacoes = limite_transacoes - 1

#                 print(f"\n\nSaque efetuado com sucesso! \n\nValor atual da sua Conta R$: {saldo:.2f} ")
#                 print(f"\n\nValor disponivel para saque diário R$: {limite_diario():.2f} ")
#     else:      
#         print(f"Saldo na conta insuficiente R$: {saldo:.2f}")  




def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_venda = 0;

    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    list_entrada = list(map(int, entrada.split(',')))

    return list_entrada

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))