
saldo = 500
opcao = ''
tentativas_diarias = 3
extrato_saque = []
extrato_deposito = []

while opcao != "x" :
    opcao = (input("Digite [s] para saque - [e] para extrato - [d] para depositar - [x] para sair: ").lower())
    if opcao == "e":
        print('\n-------------------------EXTRATO-------------------------')
        if not extrato_saque:
            print('Não foram realizados saques.')
        else:    
            print('\nHistorico de saque: ')
            [print(f'Saque realizado de: R$ {ext:.2f}')for ext in extrato_saque]
            print(f'Total sacado: R$ {sum(extrato_saque)}')

        if not extrato_deposito:
            print('\nNão foram realizados depositos.')
        else:
            print('\nHistorico de deposito: ')
            [print(f'Deposito realizado de: R$ {ext:.2f}')for ext in extrato_deposito]
            print(f'Total depositado: R$ {sum(extrato_deposito)}')

        print(f'\nSaldo atual é: {saldo:.2f}')
        print('------------------------------------------------------------')

    elif opcao == "s":
        saque = float(input(('Digite o valor a ser sacado: R$ ')))
        if saque < 0:
            (print('Valor para saque invalido.'))

        elif tentativas_diarias <1:
            print('Numero de saques diarios excedidos.')

        elif saque <= saldo and tentativas_diarias >=1:
            extrato_saque.append(saque)
            saldo-=saque
            tentativas_diarias -= 1
            print(f'Valor sacado: R$ {saque:.2f}')
            print(f'Seu saldo é: R$ {saldo:.2f}')

        elif saldo < saque:
            print("Seu saldo é insuficiente.")

    elif opcao == "d":
        
        deposito = float(input(f'Digite o valor que quer depositar: R$ '))
        if deposito > 0: 
            saldo += deposito
            extrato_deposito.append(deposito)
            print(f'Saldo atual: R$ {saldo:.2f}')
        else:
            print('Valor para deposito invalido.')

    elif opcao == "x":
        break

    else:
        print('Opção invalida.')    
