menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor que você gostária de depositar: "))

        if(deposito > 0):
            extrato += f"Depósito realizado no valor de R$ {deposito:.2f}\n"
            saldo += deposito
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Operação falhou, informe um valor maior que 0!")

    elif opcao == "s":
        saque = float(input("Digite o valor que você gostária de sacar:"))
        
        if(numero_saques < LIMITE_SAQUES):
            if(saque <= limite):
                if(saldo >= saque):
                    saldo -= saque
                    print(f"Saldo restante: R$ {saldo:.2f}")
                    extrato += f"Saque realizado no valor de R$ {saque:.2f}\n"
                    numero_saques += 1
                else:
                    print("Você não possui saldo suficiente para realizar o saque!")
            else:
                print("Você não pode realizar um saque maior que o limite da operação!")
        else:
            print('Número de saques diários chegou ao limite!')

    elif opcao == "e":
        print(f"Extrato: \n{extrato}")
        print(f"Saldo atual: R$ {saldo:.2f}")
    
    elif opcao == "q":
        print(f"Saldo atual: R$ {saldo:.2f}")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")