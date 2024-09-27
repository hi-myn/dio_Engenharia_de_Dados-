print(
    """Qual operação você deseja realizar?
        [d] - Depositar,
        [s] - Sacar,
        [e] - extrato,
        [f] - finalizar"""
)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


###### Operação de depósito ######
def operacao_deposito(valor):
    global saldo
    global extrato
    if valor <= 0:
        print("Digite um valor válido! ")

    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    return saldo


###### Operação de saque ######
def operacao_saque(valor):
    global saldo
    global numero_saques
    global extrato

    if saldo < valor:
        print("O valor inserido é maior que o saldo da conta. Saldo insuficiente.")

    elif valor > limite:
        print("O valor excede o limite permitido de R$ 500,00.")

    elif numero_saques > LIMITE_SAQUES:
        print("Número máximo de saques diários atingidio.")

    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    return saldo, numero_saques


###### Operação de extrato ######
def mostrar_extrato():
    global extrato
    print("\n=========== EXTRATO ===========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("===============================")


while True:
    opcao = input("Digite a opção: ")

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        operacao_deposito(valor)

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        operacao_saque(valor)

    elif opcao == "e":
        print("\n=========== EXTRATO ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == "f":
        print("Finalizando programa. ")
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada")
