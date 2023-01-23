# 23/01/2023 - dolar R$5,19 e euro R$5,64
real = float(input('Insira o valor em real que gostaria de converter: R$ '))
dolar = real / 5.19
euro = real / 5.64
print('Com R${} você pode comprar US${:.2f} ou €{:.2f}'.format(real, dolar, euro))
