import moeda_modulos

pre = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda_modulos.moeda(pre)} é {moeda_modulos.metade(pre, True)}')
print(f'O dobro de {moeda_modulos.moeda(pre)} é {moeda_modulos.dobro(pre, True)}')
print(f'Aumentando 10 %, temos {moeda_modulos.aumentar(pre, 10, True)}')
print(f'Diminuindo 15 %, temos {moeda_modulos.diminuir(pre, 15, True)}')
