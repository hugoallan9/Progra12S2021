
def f(n, A,B):
    respuesta = 0
    if n % 6 == 1:
        respuesta = A
    elif n % 6 == 2:
        respuesta = B
    elif n % 6 == 3:
        respuesta = B - A
    elif n % 6 == 4:
        respuesta = -A
    elif n % 6 == 5:
        respuesta = -B
    else:
        respuesta = A - B
    return respuesta

'''
T = int(input())
modulo = 10**9+ 7
for x in range(T):
    A,B,N = map(int, input().split())
    print( f(N,A,B) % modulo )
'''