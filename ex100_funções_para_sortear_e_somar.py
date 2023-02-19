from random import randint
from time import sleep
def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lst.append(n)
        print(f'{n} ', end='', flush=True)        
        sleep(0.3)
    print('PRONTO!')
    
def somaPar(lst):
    soma = 0
    for valor in lst:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lst}, temos {soma}')
    
    
numeros = list()
sorteia(numeros)
somaPar(numeros)
