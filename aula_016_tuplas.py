# As tuplas são imutáveis
'''
() = tuplas
[] = listas
{} = dicionários'''
#ex tupla
'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(len(lanche))'''

# no console vai mostrar 4, porque o comando len indica quantos elementos eu tenho na tupla
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# print(sorted(lanche)) #função sorted ordena todos elementos em ordem crescente de uma tupla, lista

# exemplo 01 colocando indices
'''For cont in range(0, len(lanche)):
	print(f'Eu vou comer {lanche[cont]} na posição {cont}')'''

# exemplo 02 colocando indices
'''for pos, comida in enumerate(lanche):
	print(f'Eu vou comer {comida} na posição {pos}')'''

# exemplo 03 - simples sem indices
'''for comida in lanche:
	print(f'Eu vou comer {comida} ')'''

#resultado exemplo 01 e 02
'''
Eu vou comer Hamburguer posição 0
Eu vou comer Suco na posição 1
Eu vou comer Pizza na posição 2
Eu vou comer Pudim na posição 3
Eu vou comer Batata Frita na posição 4'''

#resultado exemplo 03
'''
Eu vou comer Hamburguer
Eu vou comer Suco
Eu vou comer Pizza
Eu vou comer Pudim
Eu vou comer Batata Frita'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a # ira concatenar as duas tuplas começando por b
print(c.count(5)) # ira contar quantas vezes o numero 5 aparece
print(c.index(4)) # ira mostrar qual a posição do numero na tupla sempre irá parar na primeira posição alcançada
#existe a possibilidade apagar da memoria um tupla usando o comando del(tupla)
del(b)
