#calculando km percorrido e quantidade de dias alugado, usando preço do km percorrido mais a diaria
alguel = float(input("Qual o valor da diaria? R$"))
km_percorrido = float(input('Qual o valor do km percorrido? R$'))
dias = int(input('Quantos dias o veiculo foi alugado? '))
distancia = float(input('Qual o km percorrido? '))

preço = (alguel * dias) + (km_percorrido * distancia)

print('O preço a ser pago é R${:.2f}'.format(preço))