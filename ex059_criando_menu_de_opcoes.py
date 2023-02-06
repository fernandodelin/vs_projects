from time import sleep
print('Insira dois numeros ')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif opcao == 2:
        multi = n1 *n2
        print(f'A multiplicação entre {n1} e {n2} é {multi}.')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior numero é {maior}')
        elif n1 < n2:
            maior = n2
            print(f'O maior numero é {maior}')
        elif n1 == n2:
            print(f'Os numeros são iguais!')
    elif opcao == 4:
        print(f'Informe os numeros:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')