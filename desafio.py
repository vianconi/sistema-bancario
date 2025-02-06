menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operacao falhou! O valor informado e invalido.")

def saque(valor):
    global saldo, extrato, numero_saques
    if valor <= 0:
        print("Operacao falhou! O valor informado e invalido.")
        return
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print("Operacao falhou! Voce nao tem saldo suficiente.")
    elif excedeu_limite:
        print("Operacao falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operacao falhou! Numero maximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def exibir_extrato():
    print("\n======================= Extrato ====================")
    print("Nao foram realizados movimentacoes." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=======================================================")

def obter_valor(prompt):
    while True:
        try:
            valor = float(input(prompt))
            if valor < 0:
                print("O valor deve ser positivo.")
            else:
                return valor
        except ValueError:
            print("Valor invalido! Por favor, insira um numero valido.")

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = obter_valor("Informe o valor do deposito: ")
        deposito(valor)
        
    elif opcao == "s":
        valor = obter_valor("Informe o valor do saque: ")
        saque(valor)
        
    elif opcao == "e":
        exibir_extrato()
        
    elif opcao == "q":
        print("Saindo...")
        break
    
    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada.")
