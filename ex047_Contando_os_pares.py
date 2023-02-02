'''
for n in range(1, 51)
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou !') '''
num = int(input('Escolha um numero que você deseja para ver somente os pares: '))
for n in range(2, (num+1), 2):
    print(n, end=' ')
print('Acabou !')