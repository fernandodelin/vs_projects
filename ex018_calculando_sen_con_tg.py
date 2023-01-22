#calculando seno, cosseno e tangente de um ângulo
# a biblioteca math trabalha aplicando neste caso a ela vai trabalhar com radianos
from math import radians, sin, cos, tan
angulo = float(input('Digite o ãngulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tg = tan(radians(angulo))
print('O ãngulo de {} tem o SENO de {:.2f}, o COSSENO de {:.2f} e a TANGENTE de {:.2f}'.format(angulo, seno, cosseno, tg))
