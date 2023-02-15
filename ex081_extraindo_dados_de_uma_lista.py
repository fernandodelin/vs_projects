valores = []
resp = 'S'
while resp == 'S':
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
       resp = str(input('Digite S ou N: ')).strip().upper()[0]
    while resp == 'N':
      break
print('-='*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor não faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
    

