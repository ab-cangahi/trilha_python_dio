menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

 """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Lamentamos. O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Lamentamos. Seu saldo é insuficiente.")

        elif excedeu_limite:
            print("Lamentamos. Excedeu o valor de saques.")

        elif excedeu_saques:
            print("Lamentamos. Excedeu o numero de saques!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Lamentamos. O valor informado é inválido.")

    elif opcao == "e":
       
        teste_extrato = " " if not extrato else extrato

        print(f"""   ================ EXTRATO ================
                    Não foram realizadas movimentações.  {teste_extrato}
                     Saldo: R$ {saldo:.2f}
                     ==========================================
              """)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")