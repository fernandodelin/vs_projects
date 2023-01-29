# pergunte qual o valor da casa, o salario, quantos anos quer pagar, a prestação mensal não pode passar de 30% do salario.
casa = float(input('Valor da casa: R$'))
salario = float(input('Salãrio do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100 
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('A prestação será de R${:.2f}.'.format(prestação))
print('30% do seu salario {}.'.format(minimo))
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
