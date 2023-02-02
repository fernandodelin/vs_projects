#somando numeros pares
soma = 0
cont = 0
ran = int(input('Insira a quantidade numeros que deseja calcular: '))
for c in range(1, (ran+1)):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números e a soma foi {}'.format(cont, soma))

