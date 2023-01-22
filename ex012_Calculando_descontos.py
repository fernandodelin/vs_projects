# calcular desconto de 5% na compra
preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)

print('O valor R${:.2f}, com desconto de 5% será R${:.2f}'.format(preço, novo))

