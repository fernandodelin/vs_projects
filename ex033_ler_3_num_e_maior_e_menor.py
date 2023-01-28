a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# verificando quem é o menor número
if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
print('O menor numero é {}'.format(menor))
# verificando quem é o maior numero
if a > b and a > c:
    maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c
print('O maior numero é {}'.format(maior))
