'''num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    if v % 2 == 1:
        impares.append(v)
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')'''

#outra maneira de fazer
l1 = []
l2 = []
l3 = []
r = 'S'
while r == 'S':
    x = int(input('Digite um número: '))
    if x % 2 == 0 and x != 0:
        l2.append(x)
    elif x % 2 == 1 and x != 0:
        l3.append(x)
    l1.append(x)
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Digite S ou N: '))
print(f'A lista com todos os valores é {l1}')
print(f'A lista com os valores pares é {l2}')
print(f'A lista com os valores impares é {l3}')
