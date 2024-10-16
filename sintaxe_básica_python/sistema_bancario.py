from datetime import datetime

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
transacoes = []


###### Operação de depósito ######
def operacao_deposito(valor):
    global saldo
    global extrato
    global transacoes

    data_hora_atual = datetime.now()

    #filtrar transações que ocorerram no dia
    transacoes_hoje = [t for t in transacoes if t['data'].date() == data_hora_atual.date()]

    if len(transacoes_hoje) >= 10:
        print("Você excedeu o número de transações diárias.")
        return


    if valor <= 0:
        print("Digite um valor válido! ")

    else:
        transacoes.append({'valor':valor, 'data': data_hora_atual})
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    return saldo


###### Operação de saque ######
def operacao_saque(valor):
    global saldo
    global numero_saques
    global extrato
    global transacoes

    data_hora_atual = datetime.now()
    transacoes_hoje = [t for t in transacoes if t['data'].date() == data_hora_atual.date()]

    if len(transacoes_hoje) >= 10:
        print("Você excedeu o número de transações diárias.")
        return


    if saldo < valor:
        print("O valor inserido é maior que o saldo da conta. Saldo insuficiente.")

    elif valor > LIMITE:
        print("O valor excede o limite permitido de R$ 500,00.")

    elif numero_saques > LIMITE_SAQUES:
        print("Número máximo de saques diários atingidio.")

    else:
        transacoes.append({'valor': -valor, 'data': data_hora_atual, 'tipo': 'saque'})
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    return saldo, numero_saques

def calcular_saldo():
    saldo = sum([t['valor'] for t in transacoes])
    return saldo


###### Operação de extrato ######
def mostrar_extrato():
    global extrato
    print("\n=========== EXTRATO ===========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("===============================")
    if not transacoes:
        print("Não foram realizadas transações")
    else:
        for transacao in transacoes:
            valor = transacao['valor']
            tipo = transacao['tipo']
            data_hora = transacao['data'].strftime("%d-%m-%Y %H:%M:%S")
            print(f"{tipo.capitalize()}: R$ {valor:.2f} - Data e Hora: {data_hora}")
        print(f"\nSaldo atual: R$ {calcular_saldo():.2f}")


while True:
    print(
    """Qual operação você deseja realizar?
        [d] - Depositar,
        [s] - Sacar,
        [e] - extrato,
        [f] - finalizar"""
    )
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
