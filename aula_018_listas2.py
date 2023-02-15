# introdução a listas compostas
lista = [['Pedro',25]['Maria',19]['João',32]]   # agora eu tenho três listas dentro de uma
print(lista[0][0])                              # no caso irá retornar Pedro, lista 0, posição 0
print(lista[1][1])                              # no caso irá retornar 19, lista 1, posição 1
print(lista[2][0])                              # João, lista 2, posição 0
print(lista[1])                                 # vai retornar toda lista 1 = Maria, 19

lista = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in lista:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
totmai = 0
totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1 
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
