menu = """
[D] Depositar
[S] Saque
[E] Extrato
[X] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu) .upper()

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0: 
            saldo+=valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido")


    elif opcao == "S":
        valor = float(input("Informe o valor do saque: R$ "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saque excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "E":
        print("\n==========EXTRATO==========")
        print("Não fora realizados movimentações"if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "X":
        print("Obrigado por usar nosso sistema!")
        break
    else:
        print("Opção inválida, por favor selecione a opção desejada novamente!")
