# melhorando o ex035
# insira três numeros para formar um triangulo
'''Vamos acrescentar no codigo que tipo de triangulo representa:
Equilátero: todos os lados são iguais.
Isósceles: dois lados são iguais.
Escaleno: todos os lados são diferentes.'''
r1 = float(input('Primeira linha: '))
r2 = float(input('Segunda linha: '))
r3 = float(input('Terceira linha: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As linhas acima podem formar um triângulo ', end='')
    if r1 == r2 == r3 == r1:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('As linhas acima não podem formar um triângulo!')