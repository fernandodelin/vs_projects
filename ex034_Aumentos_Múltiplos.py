#valores superior a 1250 calcule um aumento de 10% e para valores iguais ou inferiores calcule 15%
valor = float(input('Qual é o valor? '))
if valor <= 1250:
    novo = valor + (valor * 15 / 100)
else:
    novo = valor + (valor * 10 / 100)
print('Se o valor <= 1250 aumento de 15%')
print('Se o valor > 1250 aumento de 10%')
print('O valor {} terá o aumento de {}'.format(valor, novo))
 