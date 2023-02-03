# define se a pessoa é maior de idade ou não de acordo com o ano insderido
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
quantde = int(input('Quantas pessoas você deseja pesquisar: '))
for pess in range(1, (quantde+1)):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    #print('Essa pessoa tem {} anos'.format(idade))
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade e {} menores.'.format(totmaior, totmenor))