
def multiplicacion(a,b):
    #a*b = a + a*(b-1)
    if b == 1:
        return a
    else:
        return a + multiplicacion(a,b-1)

def imprimir_numeros(n):
    if n == 1:
        pass
    else:
        print(n - 1)
        imprimir_numeros(n-1)


imprimir_numeros(10)
