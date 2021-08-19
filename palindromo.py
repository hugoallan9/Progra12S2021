#Palindromo son las que se leen igual de derecha a izquierda que de izquierda a derecha
#reconocer es palindromo

def es_palindromo(oracion):
    def a_caracteres(oracion):
        oracion = oracion.lower()
        respuesta = ''
        for c in oracion:
            if c in 'abcdefghijklmnñopqrstuvwxyz':
                respuesta += c
        return respuesta

    def es_pal(oracion):
        if len(oracion) <= 1:
            return True
        else:
            return oracion[0] == oracion[-1] and es_pal(oracion[1:-1])

    return es_pal(a_caracteres(oracion))

print(es_palindromo('Amor a roma'))
