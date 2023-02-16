ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8.1f}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f)
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de aluno? (999 finaliza)'))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<<< ATÉ LOGO >>>>>')