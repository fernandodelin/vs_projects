'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
Qual é o total gasto na compra.
Quantos produtos custam mais de R$1000.
Qual é o nome do produto mais barato.'''
total = 0 
totmil = 0
menor = 0
cont = 0
barato = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total += preço 
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${total:.2f}')
print(f'A quantidade de produtos acima de mil reais é {totmil}.')
print(f'O produto mais barato foi {barato} que custa R${menor}')
