# Calcular Tempo de Execução
from time import time
 
inicio = time()
 
def fatorial(numero):
    total = 1
    for i in range(1, numero+1):
        total *= i
    return total
 
print(fatorial(6))
final = time()
print(f'O tempo total em segundos foi {final-inicio}')

# Cuidando das exceções
def divide_valor(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print('Impossivel dividir por zero')
    except Exception as e:
        print(f'Erro desconhecido: {e}')
 
divide_valor(2, 1)
divide_valor(2, 0)
divide_valor(2, 'a')