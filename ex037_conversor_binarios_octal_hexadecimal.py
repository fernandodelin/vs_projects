numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)))
elif opção == 3:
    print('{} convervido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)))
else:
    print('Opção inválida. Tente novamente.')