sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] #.upper()[0] representa que ira utilizar somente a 1ª letra digitada
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} resgistrado com sucesso')
