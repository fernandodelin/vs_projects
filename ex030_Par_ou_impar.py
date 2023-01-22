# analisando o numero vai dizer se é par ou impar
numero = int(input('Me diga um número: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))
