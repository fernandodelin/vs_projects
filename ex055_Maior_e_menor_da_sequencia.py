maior = 0
menor = 0
quantde = int(input('Quantas pessoas você irá analisar: '))
for p in range(1, (quantde+1)):
    peso = float(input(f'Peso da {p}ª pessoa Kg:'))
    if p == 1:              
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg.')
print(f'O menor peso lido foi de {menor}Kg.')

'''lembrando que maior e menor, apartir do momento que inserir
o primeiro valor ele será ambos pois ate o momento so existe um valor'''