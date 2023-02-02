# usando for refazendo o ex009
n = int(input('Insira um numero para ver a tabuada: '))
print('-'*14)
for c in range(1, 11):
    print('{} X {:2}  = {}'.format(n, c, n*c))
print('-'*14)