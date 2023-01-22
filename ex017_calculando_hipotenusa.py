#calculando a hipotenusa usando biblioteca math
from math import hypot
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adj = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adj)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
