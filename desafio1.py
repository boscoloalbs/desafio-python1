#Apresentação do menu para o usuário
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

#Variáveis 
saldo = 0 
limite = 500
extrato = [""]
numero_saques = 0 
LIMITE_SAQUES = 3 
i = LIMITE_SAQUES
saque = 0

#Laço de Repetição para executar as funções até que o usuário digite "q" para parar a estrutura.
while True:
    print(menu) 
    opcao = input("Digete sua opção: ")
    #Operação de Depósito
    if opcao == "d":
        print("Deposito")
        deposito = float(input("Digite o valor que deseja depositar: "))
        saldo = saldo + deposito
        extrato.append("Depósito: + R${:.2f}" .format(deposito))
        print("O seu saldo atual é: R$ {:.2f}" .format(saldo))

    #Operação de Saque
    elif opcao == "s": 
        print("Sacar")
        if saque <= saldo and i >= 1:
            saque = float(input("Digite o valor que deseja sacar: "))
            if saque <= 500:
                i = i - 1
                saldo = saldo - saque
                extrato.append("Saque: - R${:.2f}" .format(saque))
                print("Saque efetuado com sucessod! O seu saldo atual é: R$ {:.2f}" .format(saldo))
            else:
                print("O seu limite de saque é de apenas R$ 500.00!")
        elif i <= 0:
            print("Você atingiu o limite diário de 3 operações! Aguarde 24H para realizar sua operação!")
        else:
            print("Você não possui saldo suficiente para esta operação!")

    #Operação de Extrato
    elif opcao == "e":
        print("\n================= Extrato ===================")
        print(f"\n -> {extrato}")
        print("\nSaldo: R$ {:.2f}" .format(saldo))
        print("=============================================")

    #Operação para sair do Programa
    elif opcao == "q": 
        break
    #Operação para validar que enquanto o usuário não digitar uma opção válida, a estrutura continue rodando
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")




