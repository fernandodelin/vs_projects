'''primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    print('{} '.format(c), end='- ')
print('Acabou')'''

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} - ', end='')
    termo += razão
    cont += 1
print('FIM')   