# f_n = f_{n-1} + f_{n-2} para n >= 2 f_1 = f_0 = 1
import time
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#21
'''
inicio = time.time()
print(fibonacci(200))
fin = time.time()
print('El tiempo de ejecución fue', fin  - inicio )
'''
def fibonacci2(n):
    acumuladora1 = 0
    acumuladora2 = 1
    for x in range(1,n+1):
        acumuladora2, acumuladora1 = acumuladora1 + acumuladora2, acumuladora2
    return acumuladora2

def fibonacci_mejorado(n, d):
    if n in d:
        return d[n]
    else:
        respuesta = fibonacci_mejorado(n-1,d) + fibonacci_mejorado(n-2,d)
        d[n] = respuesta
        return respuesta

d = {1:1,2:1}
print(fibonacci_mejorado(10,d))
print(d)
