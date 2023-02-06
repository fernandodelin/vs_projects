resp = 'S'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor 
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} numeros e a média é: {media}')
print(f'O maior valor foi {maior} e o menor {menor}.')
print('Acabou')