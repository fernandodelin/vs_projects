from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(print('{:=^40}'.format(' JO KEN PO ')))
print('''Suas oções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
sleep(1)
print('=-' * 20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-' * 20)
if computador == 0:# computador jogou pedra.
    if jogador == 0: # jogador jogou pedra
        print('EMPATE !')
    elif jogador == 1: # jogador jogou papel.
        print('JOGADOR VENCEU !')
    elif jogador == 2: # jogador jogou tesoura.
        print('COMPUTADOR VENCEU !')
    else:
        print('Jogada inválida')
elif computador == 1: # computador jogou papel.
    if jogador == 0: # jogador jogou pedra
        print('COMPUTADOR VENCEU!')
    elif jogador == 1: # jogador jogou papel.
        print('EMPATE!')
    elif jogador == 2: # jogador jogou tesoura.
        print('JOGADOR VENCEU!')
    else:
        print('Jogada inválida')
elif computador == 2: # computador jogou tesoura.
    if jogador == 0: # jogador jogou pedra
        print('JOGADOR VENCEU!')
    elif jogador == 1: # jogador jogou papel.
        print('COMPUTADOR VENCEU!')
    elif jogador == 2: # jogador jogou tesoura.
        print('EMPATE!')
    else:
        print('Jogada inválida')
        