# mostrando o primeiro e utlimo nome
nome = str(input('Qual é o seu nome completo: ')).strip()
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))
