import random
import math
from problemaCHN08Mejorado_23 import resolver_recurrencia2
from problemaCHN08Simplificado_24 import f

w1 = 0.5 + 1j * math.sqrt(3) / 2
w2 = 0.5 - 1j * math.sqrt(3) / 2

T = random.randint(1,10**5)
modulo = 10**9+ 7
for _ in range(T):
    A = random.randint(-10**9,10**9)
    B = random.randint(-10**9,10**9)
    N = random.randint(1,10**9)
    c = resolver_recurrencia2(A, B)
    resultado1 = int(round((c[0]*w1**N + c[1]*w2**N).real) % modulo )
    resultado2 = f(N,A,B) %modulo
    if  resultado1 != resultado2  :
        print(A,B,N)
        print('Resultado 1 es ', resultado1, 'Resultado 2 es ', resultado2)
