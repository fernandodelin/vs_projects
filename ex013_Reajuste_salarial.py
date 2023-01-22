#programa que calcula reajuste salarial
porcentagem = int(input('Insira o valor da porcentagem que deseja calcular: '))
salario = float(input('Qual é o salario? R$'))
novo = salario + (salario * porcentagem / 100)
print('O salário R${:.2f}, com {}% deaumento, será R${:.2f}'.format(salario, porcentagem, novo))
