jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()                                 #sempre tem que limpar os registro por causa do loop infinito
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())                                     # no final do processo criar uma copia da lista para o dicionario 
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(' cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')           #cabeçalho da tabela
print()
print('-='*30)
for k, v in enumerate(time):            #enumerate porque é uma lista, e ele só se aplica a lista 
    print(f'{1+k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {1+i} fez {g} gols.')
    print('-'*30)
print('<< VOLTE SEMPRE! >>')
