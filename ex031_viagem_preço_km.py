# calculando preço da passagem e por km a ser percorrido
# cobra o preço R$0,50 por km para ate 200 km e R$0,45 para mais longe
distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
