num = [2, 5, 9, 1]      #criando uma lista
num [2] = 3             #alterando o valor na posição 2, no caso será o 9
num.append(7)           #comando necessário para adicionar valores a lista
num.sort                #colocando todos os numeros em ordem crescente
num.sort(reverse=True)  #colocando todos os numeros em ordem decrescente
num.insert(2, 0)        #adicionar o 0 na posição 2 empurrando os demais para frente
num.pop()               #elimina o ultimo valor da lista
num.pop(2)              #elimina o valor na posição 2
num.remove(2)           #elimina o valor 2 na primeira posição encontrada
print(num) 
print(f'Essa lista tem {len(num)} elementos.')      #print mostra a quantidade de elementos na lista
#-----------------------------------------------------------------------------------------------------------------------------------
valores = list()                                            # declarando uma lista
for cont in range(0, 5):                                    # criando uma repetição com inserção de numeros
    valores.append(int(input('Digite um valor: ')))
    
for c, v in enumerate(valores):                             # estrutura de repetição duas declarações c contando a posição
    print(f'Na posição {c} encontrei o valor {v}!')         # v dentro da função enumerate que retorna ao valor
print('Fim da lista')
#---------------------------------------------------------------------------------------------------------------------------------
a = [2, 3, 4, 7]                # declarando uma lista 
b = a                           # equiparando a lista
b[2] = 8                        # nesta alteração da posição 2 para o numero 8, isso ira afetar ambas
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]                # declarando uma lista 
b = a[:]                        # neste caso está criando uma copia da lista
b[2] = 8                        # nesta alteração da posição 2 para o numero 8, somente da lista b
print(f'Lista A: {a}')
print(f'Lista B: {b}')
#-----------------------------------------------------------------------------------------------------------------------------