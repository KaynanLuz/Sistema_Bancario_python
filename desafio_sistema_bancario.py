
menu = """\n\n ------------Bem vindo ao Banco Nampão Bank---------------

[1] Depositar
[2] Sacar 
[3] Extrato
[0] Sair

=> """

valor_deposito = 0;
valor_saque = 0;
total_conta = 0;
limite_diario = 1500;
comprovante = [];

while True:

    opcao = input(menu)

    if opcao == "1":

        valor_deposito = int(input("Deposite o valor desejado R$: "))

        if valor_deposito <= 0:
            print("\nValor Inválido!")

        else:
            total_conta += valor_deposito;    
            comprovante.append(f"Depósito: R$ {valor_deposito:.2f}")

            print(f"\n\nDeposito efetuado com sucesso! \n\nValor atual da sua Conta R$: {total_conta:.2f} ")
        
    elif opcao == "2":     

        if total_conta > 0:

            print(f"Limite maximo de saque diário R$: {limite_diario:.2f}\n\n")

            print(f"Valor atual da sua conta R$: {total_conta:.2f}\n\n")   
             
            valor_saque = int(input("Quanto deseja sacar? "))

            if valor_saque > total_conta:

                print("Não foi possivel realizar o saque, valor de saque maior do que contém na conta")

            elif valor_saque > limite_diario:
                print("Limite diário máximo excedido!!!") 

            else:
                total_conta -= valor_saque
                limite_diario -= valor_saque
                comprovante.append(f"Saque: R$ {valor_saque:.2f}")

                print(f"\n\nSaque efetuado com sucesso! \n\nValor atual da sua Conta R$: {total_conta:.2f} ")
                print(f"\n\nValor disponivel para saque diário R$: {limite_diario:.2f} ")
        
        else:      
            print(f"Saldo na conta insuficinte R$: {total_conta:.2f}")    

    elif opcao == "3":

        if comprovante:
            print("\n----------- EXTRATO -----------")
            for transacao in comprovante:
                print(transacao)
            print(f"\nSaldo atual na conta: R$ {total_conta:.2f}")
            print("-------------------------------")
        else:
            print("\nNão foram realizadas movimentações.")
    
    elif opcao == "0":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida, tente novamente!")