#detecta se a palavra é a mesma de tras pra frente
frase = str(input('Digite uma frase: ')).strip().upper() #eliminei espaços antes e depois da str colocando em caixa alta tudo
palavras = frase.split()        #Eliminando espaços entre as palavras e transformando em coleção
junto = ''.join(palavras)       #juntando todas as palavras digitadas

'''inverso = ''
for letra in range(len(junto) -1, -1, -1): #inverte a str
    inverso += junto[letra]'''

inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
