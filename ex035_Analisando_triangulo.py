# insira três numeros para formar um triangulo
r1 = float(input('Primeira linha: '))
r2 = float(input('Segunda linha: '))
r3 = float(input('Terceira linha: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As linhas acima podem formar um triângulo!')
else:
    print('As linhas acima não podem formar um triângulo!')
 