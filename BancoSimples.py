menu = """

Digite a operação desejada:
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Sair

"""

saldo = 0
num_saques = 0
LIMITE_SAQUE = 3
extrato = ""

while True:
    
    opcao = input(menu)

    if opcao == '1':
      depo = float(input("Informe o valor a ser depositado: "))
      if depo <= 0:
        print("Erro: Valor inválido.")
      else:
        saldo += depo
        print(f"Operação bem-sucedida.\nNovo saldo: R${saldo:.2f}.")
        extrato = extrato + f"Depósito: R${depo:.2f}\n"

    elif opcao == '2':
        
        valor = float(input("Informe o valor a ser sacado: "))
        
        if num_saques >= LIMITE_SAQUE:
            print("Erro: Limite de saques diário atingido.")
        
        elif valor <= 0 or valor > saldo:
            print(f"Erro: Valor inválido. \nSaldo total: R${saldo:.2f}.")
        
        elif valor > 500:
                print(f"Erro: Limite de saque excedido. \nSaldo total: R${saldo:.2f}.")

        else:
            saldo -= valor
            print(f"Operação bem-sucedida.\nNovo saldo: R${saldo:.2f}.")
            num_saques += 1
            extrato = extrato + f"Saque: R${valor:.2f}\n"

    elif opcao == '3':
        print("************* EXTRATO ***************")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print("*************************************")

    elif opcao == '4':
        break

    else:
        print("Operação inválida.")