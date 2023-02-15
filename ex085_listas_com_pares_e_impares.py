numero = [[], []]                                           #declarando duas listas
valor = 0                                                   #declarando variante
for c in range(1, 8):                                       #criando laço de repetição com 7 numeros
    valor = int(input(f'Digite o {c}° valor: '))        
    if valor % 2 == 0:                                      #criando condicional par
        numero[0].append(valor)                             #inserte lista par
    else:
        numero[1].append(valor)                             #inserte lista impar
print('-='*30)
numero[0].sort()                                            #ordenando lista par crescente
numero[1].sort()                                            #ordenando lista impar crescente
print(f'Os valores pares digitados foram: {numero[0]}')     #imprimindo lista par
print(f'Os valores impares digitados foram: {numero[1]}')   #imprimindo lista impar
