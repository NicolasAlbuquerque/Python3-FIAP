opcao = 0
while opcao != 4:
    print('1 - Rodar funcionalidade 1')
    print('2-  Rodar funcionalidade 2')
    print('3 - Rodar  funcionalidade 3')
    print('4 - Sair do sistema')
    opcao= int(input("Digite a opção desejada: "))

    if opcao == 1:
        print('Executando a opção 1')
    elif opcao == 2:
        print('Executando a opção 2')
    elif opcao == 3 :
        print('Executando a opção 3')
    elif opcao == 4:
        print('Saindo do sistema')
    else:
        print('Opção inválida')