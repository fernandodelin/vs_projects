#calculando o IMC
'''Abaixo de 18.5: abaixo do peso
entre 18.5 a 25: peso ideal
25 a 30: sobrepeso
30 a 40: Obesidade
Acima de 40: Obesidade mórbida'''
peso = float(input('Qual é o peso: (kg) '))
altura = float(input('Qual é a altura: (m) '))
mc = peso / (altura ** 2)
if mc < 18.5:
    print('O IMC é {:.1f} e você está abaixo do peso!'.format(mc))
elif 25 > mc >= 18.5:
    print('O IMC é {:.1f} e você está com o peso ideal! PARABÉNS !!!'.format(mc))
elif 30 > mc >= 25:
    print('O IMC é {:.1f} e você está com sobrepeso!'.format(mc))
elif 40 > mc >= 30:
    print('O IMC é {:.1f} e você está com obesidade!'.format(mc))
#elif mc >= 40:
else:
    print('O IMC é {:.1f} e você está com obesidade mórbida'.format(mc))

 