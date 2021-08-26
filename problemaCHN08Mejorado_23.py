import numpy as np
import scipy.sparse.linalg
import scipy.sparse
import math

w1 = 0.5 + 1j * math.sqrt(3) / 2
w2 = 0.5 - 1j * math.sqrt(3) / 2

def determinante(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

def resolver_recurrencia2(A,B):
    sol = []
    denominador = determinante([[w1,w2],[w1**2,w2**2]])
    sol.append(determinante([[A,w2],[B,w2**2]]) / denominador)
    sol.append(determinante([[w1,A],[w1**2,B]]) / denominador)
    return sol

def resolver_recurrencia(A,B):
    matriz = scipy.sparse.csr_matrix([[w1, w2],[w1**2,w2**2]] )
    b = np.array([A,B])
    x = scipy.sparse.linalg.spsolve(matriz,b)
    return x

'''
T = int(input())
modulo = 10**9+ 7
for x in range(T):
    A,B,N = map(int, input().split())
    c = resolver_recurrencia2(A,B)
    print( int(round((c[0]*w1**N + c[1]*w2**N).real) % modulo) )
'''