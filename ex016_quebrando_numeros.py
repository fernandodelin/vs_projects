#digite um numero real e transforme em numero inteiro
from math import trunc
numero = float(input('Digite um número real:'))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(numero, trunc(numero)))

'''
numero = float(input('Digite um número real:'))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(numero, int(numero)))
'''