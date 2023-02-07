# usando for refazendo o ex009 e ex049
while True:
    n = int(input('Insira um numero para ver a tabuada: '))
    print('-'*20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c:2}  = {n*c}')
    print('-'*20)
print('Programa encerrado.')