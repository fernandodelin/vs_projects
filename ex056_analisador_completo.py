'''O programa vai te retornar a média de idade do grupo.
Qual o nome do homem mais velho.
Quantas mulheres têm menos de 20 anos.'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
quantde = int(input('Quantas pessoas você deseja analisar: '))
for p in range(1, (quantde+1)):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
       maioridadehomem = idade
       nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
mediaidade = (somaidade / quantde)
print('A média de idade do grupo é de {:.2f} anos'.format(mediaidade))
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
