temp = []
principal = []
mai = 0
men = 0
while True:                                                         #criando um loop infinito
    temp.append(str(input('Nome: ')).strip())                       #criando dados na lista temp
    temp.append(float(input('Peso: ')))                             #criando dados na lista temp
    if len(principal) == 0:                                         # declarando se maior e menor
        mai = temp[1]
        men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]   
    principal.append(temp[:])                                       #criando uma copia da lista temp na lista principal
    temp.clear()                                                    #limpando lista temp
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  #condição de parada do loop infinito
    if resp in 'N':
        break                                                       #declaração utilizada pra parar loop
print('-='*30)
print(f'Os dados foram {principal}')                                # exibindo todos elementos da lista 
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')         # exibindo a quantidade de listas
print(f'O maior peso foi de {mai}kg. Peso de ', end='')             # exibindo valor maximo calculado no if else linha 8,15
for p in principal:                                                 # estrutura de repetição para exibir elementos de maior peso
    if p[1] == mai:                                                 
        print(f'[{p[0]}] ',end='')
print(f'\nO menor peso foi de {men}kg. Peso de ', end='')             # exibindo valor minimo calculado no if else linha 8,15
for p in principal:                                                 # estrutura de repetição exibindo elementes de maior peso
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
