# codigo ensinado na aula
'''nome = str(input('Qual o seu nome? '))
if nome == 'Fernando':
    print('Que lindo você tem!')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}'.format(nome))'''
# desafio 028
from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
