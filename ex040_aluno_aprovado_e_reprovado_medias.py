'''Calculando a media entre duas notas:
media abaixo de 5 reprovado
media entre 5 e 6.9 recuperação
media superior a 7 aprovado'''
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 < média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >=7:
    print('O aluno está APROVADO.')
