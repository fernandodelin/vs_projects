#Função está relacionada a rotina. print(), len(), input(), int() tudo é função
#Podemos criar nossa propria função
#vamos criar uma que coloque tracinho

'''def mostralinha(msg):
    print('-'*30)
    print(msg)
    print('-'*30)

    
mostralinha('   HELLO MOTHERFUCKER !    ')'''
#-------------------------------------------------------------------------------------------------
#exemplo de função para criar uma rotina
'''
a = 5
b = 8
s = a + b
print(s)

a = 8
b = 4
s = a + b
print(s)

a = 3
b = 1
s = a + b
print(s)'''

#substituir tudo por:
''' 
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    
    
soma(5, 8)
soma(8, 4)
soma(3, 1) 
soma(b=3, a=4)'''

#empacotador de numeros
'''def contador(* num): '''  #neste caso ele listas, tuplas,
# dobrando numeros
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
        

valores = [6, 4, 3, 8, 0, 9, 1, 2]
dobra(valores)
print(valores)'''
#somando numeros
'''def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
    
soma(5, 6)
soma(7, 2, 9)'''
