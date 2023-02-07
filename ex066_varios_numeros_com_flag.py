from time import sleep
numero = 0
cont = 0
soma = 0
numero = int(input('Digite um numero [999 para parar]: '))
while True:
    numero = int(input('Digite um numero [999 para parar]: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'Você digitou {cont} numeros e a soma é {soma}.')
sleep(2)
print('~'*30)
print('Acabou')