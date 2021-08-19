import math


def is_prime(numero):
    """
    Esta función es booleana y sirve para verificar si un número es primo o no.
    :param numero: Número entero positivo que se desea verificar si es primo o no.
    :return: True si el número es primo, False si el número es compuesto
    """
    retorno = False
    criba = math.floor(math.sqrt(numero) + 1)
    for x in range(2, criba):
        if numero % x == 0:
            break
        if x == criba - 1:
            retorno = True
    return retorno
