import moeda_modulos

pre = float(input('Digite o preço: R$'))
print(f'A metade de R${pre} é R${moeda_modulos.metade(pre)}')
print(f'O dobro de R${pre} é R${moeda_modulos.dobro(pre)}')
print(f'Aumentando 10%, temos R${moeda_modulos.aumentar(pre, 10)}')
print(f'Diminuindo 15%, temos R${moeda_modulos.diminuir(pre, 15)}')
